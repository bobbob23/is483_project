from __init__ import db
from sqlalchemy.orm import relationship

class Probability(db.Model):
    __tablename__ = 'Probability'
    email = db.Column(db.String(150), primary_key=True)
    overall_probability = db.Column(db.Float)
    total_working_years = db.Column(db.Float)
    num_companies_worked = db.Column(db.Float)
    education_field = db.Column(db.Float)
    education_level = db.Column(db.Float)