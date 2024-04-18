from __init__ import db
from sqlalchemy.orm import relationship

class ML_Fields(db.Model):
    __tablename__ = 'ML_Fields'
    email = db.Column(db.String(250), primary_key=True)
    total_working_years = db.Column(db.String(250))
    num_companies_worked = db.Column(db.String(250))
    education_field = db.Column(db.String(250))
    education_level = db.Column(db.String(250))