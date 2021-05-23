from flask import Blueprint, render_template, redirect, session, url_for, flash, request
from werkzeug.security import generate_password_hash

from application import db
from author.models import Author
from author.forms import RegisterForm, LoginForm

author_app = Blueprint('author_app', __name__)

@author_app.route('/register', methods=('GET', 'POST'))
def register():
    # Create a new instance of RegisterForm
    form = RegisterForm()
    if form.validate_on_submit():

        ## Activates the python debugger
        ## Windows, Mac, or Linux Only
        ## Do not use on pythonanywhere
        #import pdb; pdb.set_trace()
        
        hashed_password = generate_password_hash(form.password.data)
        author = Author(
            form.full_name.data,
            form.email.data,
            hashed_password
        )
        db.session.add(author)
        db.session.commit()
        flash("You are now registered. Please login.")
        return redirect(url_for('.login'))
    return render_template('author/register.html', form=form)
    
@author_app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        author = Author.query.filter_by(email=form.email.data).first()
        session['id'] = author.id
        session['full_name'] = author.full_name
        if 'next' in session:
            next = session.get('next')
            session.pop('next')
            return redirect(next)
        else:        
            return redirect(url_for('blog_app.index'))

    return render_template('author/login.html', form=form, error=error)

@author_app.route('/logout')
def logout():
    if session.get('id'):
        session.pop('id')
        session.pop('full_name')
        flash("You are logged out.")
        return redirect(url_for('.login'))
    else:
        return redirect(url_for('blog_app.index')) 