from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash

from contact.forms import ContactForm
from author.decorators import login_required
from contact.mail_sender import send_mail

contact_app = Blueprint('contact_app', __name__)


@contact_app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        if form.name.data and form.email.data and form.message.data:
            name = form.name.data
            email = form.email.data
            message = form.message.data
            print(name, email, message)
            try:
                send_mail(name, email, message)
                flash("Your message was sent.  Thank you.")
                return redirect(url_for('.contact'))
            except Exception as e:
                flash(
                    'Sorry, your message could not be sent.  Please try again.', 'error')
    return render_template('contact/contact.html', form=form)
