#.
#imprtflsk

#frmflsk

from flask import Flask
#imprt_sqlachmy

from flask_sqlalchemy import SQLAlchemy
#import_os
from os import path
#.
#login_mangr
from flask_login import LoginManager

db = SQLAlchemy()

#db_nam_e
DB_NAME = "database.db"

#def_app
def create_app():
    app = Flask(__name__)
#.
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#/  
    db.init_app(app)

#imprt_views
    from .views import views
#auth
    from .auth import auth
#


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
#login_mangr
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
#.

    return app

#.
#create_dataset

def create_database(app):
    if not path.exists('website/' + DB_NAME):
#db_create
        db.create_all(app=app)
        print('Created Database!')
#.
