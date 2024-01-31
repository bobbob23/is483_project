from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from decouple import config, UndefinedValueError

app = Flask(__name__)

db_username = 'root'
db_password = ''
port = '3306'
db_name = 'tsh_db'

# INSERT SQL URL
db_uri = f'mysql://{db_username}:{db_password}@localhost:{port}/{db_name}'
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
except UndefinedValueError:
    app.config['SQLALCHEMY_DATABASE_URI'] = None

app.secret_key = 'asdfghjkl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from routes.applicantRoute import *
from routes.jobListingRoute import *
# Register routes
app.register_blueprint(applicant_routes)
app.register_blueprint(job_listing_routes)
