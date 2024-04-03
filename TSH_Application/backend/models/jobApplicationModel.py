from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from __init__ import db

class Job_Application(db.Model):
    __tablename__ = 'Job_Application'
    email = db.Column(db.String(250), ForeignKey('Applicant.email'), primary_key=True)
    job_ID = db.Column(db.Integer, ForeignKey('Job_listing.job_ID'), primary_key=True)
    applicant_status = db.Column(db.String(250))
    skill = db.Column(db.JSON)
    rank_probability = db.Column(db.Float)
    past_salary = db.Column(db.String(150))
    work_permit = db.Column(db.String(150))
    resume = db.Column(db.String(250))
    transcript = db.Column(db.String(250))
    reference_letter = db.Column(db.String(250))
    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))


    applicant = relationship("Applicant", back_populates="application")
    job_listing = relationship("Job_listing", back_populates="application")