from flask import redirect, url_for, request, session
from flask import jsonify
from settings import MAX_INITIAL_COMMENTS, COMMENTS_LOAD_MORE_INC 

COMMENTS_LOAD_MORE_INC
def adder(access_code):
    print(f'access code = {access_code}')
    if(access_code != 'rwd'):
        return redirect(url_for('.index'))
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)

def show_more_comments(access_code, comments):
    if(access_code != 'rwd'):
        return redirect(url_for('.index'))

    total_comments = comments.count()
    max_init_comments = int(MAX_INITIAL_COMMENTS)
    comments_inc = int(COMMENTS_LOAD_MORE_INC)
    more_comments_btn_display = True
    
    def set_count():
        if(comments.count() <= max_init_comments):
            more_comments_btn_display = False
        elif(('comments_count' not in session) and (total_comments >= max_init_comments + comments_inc)):
            session['comments_count'] = str(max_init_comments + comments_inc)
        elif(('comments_count' not in session) and (total_comments == max_init_comments + 1)):
            session['comments_count'] = str(max_init_comments + 1)
        elif(('comments_count' in session) and (int(session['comments_count']) >= total_comments)):
            more_comments_btn_display = False
        elif(('comments_count' in session) and (total_comments >= max_init_comments + comments_inc)):
            session['comments_count'] = str(int(session['comments_count']) + comments_inc)
        elif(('comments_count' in session) and (total_comments == max_init_comments + 1)):
            session['comments_count'] = str(int(session['comments_count']) + 1)
        return int(session['comments_count'])

    offset = set_count() - comments_inc

    if( ('comments_count' in session) and (int(session['comments_count']) >= total_comments) ):
        more_comments_btn_display = False

    comments = comments.limit(comments_inc).offset(offset);
    # name_list = []
    # email_list = []
    # comment_list = []
    # comment_date_list = []
    # avatar_hash_list = []
    comment_html_list = []

    for comment in comments:
        comment_html = f'<div class="comment"><div class="comment--metadata"><div class="comment--avatar"><img class="comment--avatar" src="https://www.gravatar.com/avatar/{comment.avatar_hash}?s=75&r=pg&d=mp" /></div><div class="comment--name-and-date"><div class="comment--name-container"><span class="comment--name">{comment.name}</span></div><div class="comment--date-container"><span class="comment--date">{comment.comment_date}</span></div></div></div><div class="comment--feedback-container"><p class="comment--feedback">{comment.comment}</p></div></div>'

        # name_list.append(comment.name)
        # email_list.append(comment.email)
        # comment_list.append(comment.comment)
        # comment_date_list.append(comment.comment_date)
        # avatar_hash_list.append(comment.avatar_hash)
        comment_html_list.append(comment_html)
        
    results_dict =  {
                    # 'name_list': name_list,
                    # 'email_list': email_list,
                    # 'comment_list': comment_list,
                    # 'comment_date_list': comment_date_list,
                    # 'avatar_hash_list': avatar_hash_list,
                    'comment_html_list': comment_html_list,
                    'more_comments_btn_display': more_comments_btn_display
                    }
    return jsonify(result=results_dict)

def clear_comments_count_session():
    if 'comments_count' in session:
        session.pop('comments_count', None)
    max_initial_comments = MAX_INITIAL_COMMENTS
    results_dict = {'max_initial_comments': max_initial_comments}
    return jsonify(result=results_dict)

def set_blog_category(cat):
    print ('CAT = ', cat)
    results_dict = {}
    if cat == 'All':
        if ('blog_category' in session):
            session.pop('blog_category', None)
    elif (('blog_category' in session) and (session['blog_category'] != cat) or ('blog_category' not in session)):
        session['blog_category'] = cat
    if 'blog_category' in session:
        print('SESSION = ', session['blog_category'])
    else:
        print ('NO SESSION')
    return jsonify(result=results_dict)