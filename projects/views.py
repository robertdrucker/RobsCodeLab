from flask import Blueprint, render_template, redirect, url_for

projects_app = Blueprint('projects_app',  __name__)


@projects_app.route('/projects/gallery/wings')
def photo_gallery_wings():
    return render_template('projects/gallery_wings_albums.html')
