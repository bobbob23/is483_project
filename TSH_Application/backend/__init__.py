from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from decouple import config, UndefinedValueError
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)

DB_URI = os.environ["DB_URI"]

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
except UndefinedValueError:
    app.config['SQLALCHEMY_DATABASE_URI'] = None

app.secret_key = 'asdfghjkl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.config['CORS_HEADERS'] = 'Content-Type'

from routes.applicantRoute import *
from routes.jobListingRoute import *
# Register routes
app.register_blueprint(applicant_routes)
app.register_blueprint(job_listing_routes)
