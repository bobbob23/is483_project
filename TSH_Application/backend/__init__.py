from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from decouple import config, UndefinedValueError
import os
# from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

# load_dotenv()

app = Flask(__name__)
# DB_URI = os.environ["DB_URI"]

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


try:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
except UndefinedValueError:
    app.config['SQLALCHEMY_DATABASE_URI'] = None

app.secret_key = 'asdfghjkl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, origins='*')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.config['CORS_HEADERS'] = 'Content-Type'

from routes.applicantRoute import *
from routes.jobListingRoute import *
# Register routes
app.register_blueprint(applicant_routes)
app.register_blueprint(job_listing_routes)
