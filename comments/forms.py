from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, TextAreaField, ValidationError
from wtforms.fields.html5 import EmailField
from werkzeug.security import check_password_hash

class CommentForm(FlaskForm):
    name = StringField('Full Name', [validators.InputRequired()])
    email = EmailField('Email Address', [validators.InputRequired(), validators.Email()])
    comment = TextAreaField('Comment', validators=[validators.InputRequired(), validators.Length(min=3)])
