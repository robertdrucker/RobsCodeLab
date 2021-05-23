from datetime import datetime

from application import db

# Association table
tag_x_post = db.Table('tag_x_post',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    image = db.Column(db.String(36))
    image_alt = db.Column(db.String(255))
    slug = db.Column(db.String(255), unique=True) # Max for varchar indexes
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)

    # Whenever you are creating any model, put the definition relationships
    #   on the table that is the "many". 

    # example: post_author = post.author.full_name   (one to one relationship)

    # Puts a posts property on the author object
    # example: all_posts_by_author = author.posts   (one to many relationship)
    author = db.relationship('Author',
                                backref=db.backref('posts', lazy='dynamic'))

    category = db.relationship('Category',
                                backref=db.backref('posts', lazy='dynamic'))

    tags = db.relationship('Tag', secondary=tag_x_post, lazy='subquery',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, author, title, body, image=None, image_alt=None, category=None,
        slug=None, publish_date=None, live=True):
        self.author_id = author.id
        self.title = title
        self.body = body
        self.image = image
        self.image_alt = image_alt
        if category:
            self.category_id = category.id
        self.slug = slug
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        self.live = live

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
