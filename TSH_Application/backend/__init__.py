from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
# from decouple import UndefinedValueError
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from models import *

load_dotenv()

app = Flask(__name__)
DB_URI = os.environ["DB_URI"]

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# except UndefinedValueError:
#     app.config['SQLALCHEMY_DATABASE_URI'] = None


ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["SECRET_ACCESS_KEY"]

app.secret_key = 'asdfghjkl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, origins='*')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.config['CORS_HEADERS'] = 'Content-Type'

from routes.applicantRoute import *
from routes.jobListingRoute import *
from routes.jobApplicationRoute import *
from routes.dashboardRoute import *
from routes.autoFillRoute import *
# Register routes
app.register_blueprint(applicant_routes)
app.register_blueprint(job_listing_routes)
app.register_blueprint(job_application_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(autofill_routes)