from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_avatars import Avatars

# Comment out before running tests
from flaskext.markdown import Markdown

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# setup db
db = SQLAlchemy()


def create_app(**config_overrides):
    app = Flask(__name__)
    print(f'From /application.py create_app, __name__ = {__name__}')

    avatars = Avatars(app)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    # Comment out before running tests
    Markdown
    Markdown(app)

    # import blueprints
    from blog.views import blog_app
    from author.views import author_app
    from contact.views import contact_app
    from projects.views import projects_app

    # register blueprints
    app.register_blueprint(blog_app)
    app.register_blueprint(author_app)
    app.register_blueprint(contact_app)
    app.register_blueprint(projects_app)

    # Setup route for about page
    @app.route('/about')
    def about():
        return render_template('/about/about.html')

    # Setup route for contact page
    # @app.route('/contact')
    # def contact():
    #     return render_template('/contact/contact.html')

    @app.errorhandler(404)
    def page_not_found(e):
        if 'blog_category' in session:
            session.pop('blog_category', None)
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    return app
