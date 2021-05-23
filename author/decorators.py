from functools import wraps
from flask import session, request, redirect, url_for, abort, flash
import inspect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('id') is None:
            flash('Please login to continue')
            print(f'args = {args}, kwargs= {kwargs}')
            print(f'request.url = {request.url}')
            return redirect(url_for('author_app.login', next=request.url))
        return f(*args, **kwargs)
        
    return decorated_function