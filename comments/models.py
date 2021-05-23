from datetime import datetime

from application import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    avatar_hash = db.Column(db.String(80))
    comment = db.Column(db.Text)
    comment_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)

    # Whenever you are creating any model, put the definition relationships
    #   on the table that is the "many". 

    # example: post_author = post.author.full_name   (one to one relationship)

    # Puts a posts property on the author object
    # example: all_posts_by_author = author.posts   (one to many relationship)

    post = db.relationship('Post', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, post_id, name, email, avatar_hash,
        comment, comment_date=None, live=False):
        self.post_id = post_id
        self.name = name
        self.email = email
        self.avatar_hash = avatar_hash
        self.comment = comment
        if comment_date is None:
            self.comment_date = datetime.utcnow()
        self.live = live

    def __repr__(self):
        return '<Post %r>' % self.name
