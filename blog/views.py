from flask import Blueprint, session, render_template, flash, redirect, url_for, request
from slugify import slugify
import uuid
import os
from application import Avatars
import hashlib
from PIL import Image
from flask import jsonify

from application import db
from blog.models import Post, Category, Tag
from blog.forms import PostForm
from author.models import Author
from author.decorators import login_required
from comments.models import Comment
from comments.forms import CommentForm
from settings import BLOG_POST_IMAGES_PATH, MAX_INITIAL_COMMENTS
from pyfiles._helpers import *

blog_app = Blueprint('blog_app',  __name__)

POSTS_PER_PAGE = 5

valid_blog_categories = ['CSS', 'HTML', 'JavaScript', 'Python', 'SQL']


@blog_app.route('/')
def index():
    if (('blog_category' in session) and (session['blog_category'] in valid_blog_categories) and session['blog_category'] != 'All'):
        return redirect(url_for('.category_by_name', category=session['blog_category']))

    page = int(request.values.get('page', '1'))

    # Use of SQLAlchemy data chain
    posts = Post.query.filter_by(live=True).order_by(Post.publish_date.desc())\
        .paginate(page, POSTS_PER_PAGE, False)
    comments = Comment.query.filter_by(live=True)

    return render_template('blog/index.html',
                           posts=posts,
                           comments=comments,
                           title='Recent Posts'
                           )


@blog_app.route('/post', methods=('GET', 'POST'))
# @login_required
def post():
    if session.get("id") is None:
        return redirect(url_for('blog_app.index'))

    form = PostForm()
    tags_field = request.values.get('tags_field')

    if form.validate_on_submit():

        if form.image.data:
            image = form.image.data

        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)

            # Gives the category id
            # Doesn't save the data on disk, but does do sort of
            #   a pre-save that does generate the potential id
            #   and keeps the session operating for other writes
            #   or updates.
            db.session.flush()
            # Assigns the proper category id to the category variable.
            category = new_category
        else:
            category = form.category.data

        author = Author.query.get(session['id'])
        title = form.title.data.strip()
        body = form.body.data.strip()
        post = Post(
            author=author,
            title=title,
            body=body,
            image=image,
            category=category,
        )

        _save_tags(post, tags_field)

        db.session.add(post)
        db.session.commit()

        slug = slugify(str(post.id) + '-' + post.title)
        post.slug = slug
        db.session.commit()

        flash('Article posted')
        return redirect(url_for('.article', slug=slug))

    return render_template('blog/post.html',
                           form=form,
                           action="new",
                           tags_field=tags_field
                           )


@blog_app.route('/posts/<slug>', methods=('GET', 'POST'))
def article(slug):
    if 'comments_count' in session:
        session.pop('comments_count', None)
    post = Post.query.filter_by(slug=slug).first_or_404()
    category = Category.query.filter_by(id=post.category_id).first_or_404()
    comments = Comment.query.filter_by(
        post_id=post.id, live=True).order_by(Comment.comment_date.desc())
    comments_total = comments.count()
    comments = comments.limit(MAX_INITIAL_COMMENTS)

    posts = Post.query.filter_by(live=True).order_by(Post.publish_date.desc())

    for comment in comments:
        print((f'comment.comment = {comment.comment}'))

    form = CommentForm()

    if form.validate_on_submit():
        post_id = post.id
        name = form.name.data.strip()
        email = form.email.data.strip()
        avatar_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
        print(f'avatar_hash={avatar_hash}')
        comment = form.comment.data.strip()

        comment = Comment(
            post_id=post_id,
            name=name,
            email=email,
            avatar_hash=avatar_hash,
            comment=comment,
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comment received and pending approval. Thank you.')
        return redirect(url_for('.article', slug=post.slug))

    return render_template('blog/article.html',
                           post=post,
                           category=str(category),
                           comments=comments,
                           comments_total=comments_total,
                           max_initial_comments=int(MAX_INITIAL_COMMENTS),
                           form=form
                           )


@blog_app.route('/edit/<slug>', methods=('GET', 'POST'))
@login_required
def edit(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    form = PostForm(obj=post)
    tags_field = request.values.get('tags_field', _load_tags_field(post))

    if form.validate_on_submit():
        original_title = post.title
        form.populate_obj(post)

        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            post.category = new_category

        if form.title.data != original_title:
            post.slug = slugify(str(post.id) + '-' + form.title.data)

        _save_tags(post, tags_field)

        db.session.commit()
        # flash('Article edited')
        return redirect(url_for('.article', slug=post.slug))

    return render_template('blog/post.html',
                           form=form,
                           post=post,
                           action="edit",
                           tags_field=tags_field
                           )


@blog_app.route('/delete/<slug>')
@login_required
def delete(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    post.live = False
    db.session.commit()
    flash("Article deleted")
    return redirect(url_for('.index'))


@blog_app.route('/categories/<category_id>')
def categories(category_id):
    category = Category.query.filter_by(id=category_id).first_or_404()
    page = int(request.values.get('page', '1'))
    posts = Post.query.filter_by(category=category, live=True)\
        .order_by(Post.publish_date.desc())\
        .paginate(page, POSTS_PER_PAGE, False)
    return render_template('blog/category_posts.html',
                           posts=posts,
                           title=category,
                           category_id=category_id
                           )


@blog_app.route('/category/<category>')
def category_by_name(category):
    if (category == 'All'):
        return redirect(url_for('.index'))
    category = Category.query.filter_by(name=category).first_or_404()
    page = int(request.values.get('page', '1'))
    posts = Post.query.filter_by(category=category, live=True)
    if posts.count() < 1:
        return render_template('404.html'), 404
    posts = posts.order_by(Post.publish_date.desc())\
        .paginate(page, POSTS_PER_PAGE, False)
    comments = Comment.query.filter_by(live=True)
    return render_template('blog/index.html',
                           posts=posts,
                           comments=comments,
                           title='Recent Posts',
                           category=category,
                           )


@blog_app.route('/category/<category>/tag/<tag>')
def category_and_tag(tag, category):
    if (category == 'All'):
        return redirect(url_for('.index'))
    category = Category.query.filter_by(name=category).first_or_404()
    category_id = category.id
    tag = Tag.query.filter_by(name=tag).first_or_404()
    page = int(request.values.get('page', '1'))
    posts = tag.posts.filter_by(category_id=category_id, live=True)
    if posts.count() < 1:
        return render_template('404.html'), 404
    posts = posts.order_by(Post.publish_date.desc())\
        .paginate(page, POSTS_PER_PAGE, False)
    comments = Comment.query.filter_by(live=True)
    return render_template('blog/index.html',
                           posts=posts,
                           comments=comments,
                           title='Recent Posts',
                           tag=tag,
                           category=category,
                           )


@blog_app.route('/tag/<tag>')
def tags(tag):

    if (('blog_category' in session) and (session['blog_category'] in valid_blog_categories) and session['blog_category'] != 'All'):
        category = session['blog_category']
        category_result = Category.query.filter_by(
            name=category).first_or_404()
        category_id = category_result.id
    else:
        category_id = False
        category = 'All'
    tag = Tag.query.filter_by(name=tag).first_or_404()
    page = int(request.values.get('page', '1'))
    if (category_id):
        posts = tag.posts.filter_by(category_id=category_id, live=True)\
            .order_by(Post.publish_date.desc())\
            .paginate(page, POSTS_PER_PAGE, False)
        comments = Comment.query.filter_by(live=True)
    else:
        posts = tag.posts.filter_by(live=True)\
            .order_by(Post.publish_date.desc())\
            .paginate(page, POSTS_PER_PAGE, False)
        comments = Comment.query.filter_by(live=True)
    return render_template('blog/index.html',
                           posts=posts,
                           comments=comments,
                           title='Recent Posts',
                           tag=tag,
                           category=category
                           )


def _image_resize(original_file_path, image_id, image_base, extension):
    file_path = os.path.join(
        original_file_path, image_id + '.png'
    )
    image = Image.open(file_path)
    wpercent = (image_base / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((image_base, hsize), Image.ANTIALIAS)
    modified_file_path = os.path.join(
        original_file_path, image_id + '.' + extension + '.png'
    )
    image.save(modified_file_path)
    return


def _save_tags(post, tags_field):
    post.tags.clear()
    for tag_item in tags_field.split(','):
        tag = Tag.query.filter_by(name=slugify(tag_item)).first()
        if not tag:
            tag = Tag(name=slugify(tag_item))
            db.session.add(tag)
        post.tags.append(tag)
    return post


def _load_tags_field(post):
    tags_field = ''
    for tag in post.tags:
        tags_field += tag.name + ', '
    return tags_field[:-2]

# Activated by ajax call


@blog_app.route('/load_more_comments/<slug>')
def comment_loader(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    comments = Comment.query.filter_by(
        post_id=post.id, live=True).order_by(Comment.comment_date.desc())
    print(f'request.args = {request.args}')
    access_code = request.args.get('access_code', '', type=str)
    # python helpers function
    return show_more_comments(access_code, comments)

# Activated by ajax call


@blog_app.route('/clear_comments_count')
def clear_comments_count():
    # python helpers function
    return clear_comments_count_session()

# Activated by ajax call


@blog_app.route('/blog_category/<category>')
def category_session(category):
    return set_blog_category(category)
