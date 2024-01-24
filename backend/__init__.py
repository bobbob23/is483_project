from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfghjkl'

    # INSERT SQL URL
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sql'
    db.init_app(app)

    from .controller.homeRoute import homes

    app.register_blueprint(homes, url_prefix='/')

    from .models import Applicant
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('webdsite/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')