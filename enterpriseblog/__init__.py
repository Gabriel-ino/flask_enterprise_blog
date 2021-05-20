# enterpriseblog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required

app = Flask(__name__)

############################################################################
#
#                                 LOGIN CONFIGS
#
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

############################################################################
#
#
#                          CREATING DATABASE
#
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
#
############################################################################

db = SQLAlchemy(app)
db.drop_all()
db.create_all()
Migrate(app, db)


from enterpriseblog.core.views import core
from enterpriseblog.users.views import users
from enterpriseblog.error_pages.handlers import error_pages
from enterpriseblog.blog_posts.forms import BlogPostForm
from enterpriseblog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)


