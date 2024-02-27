from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from __init__ import db

class Job_Application(db.Model):
    __tablename__ = 'Job_Application'
    email = db.Column(db.String(250), ForeignKey('Applicant.email'), primary_key=True)
    job_ID = db.Column(db.Integer, ForeignKey('Job_listing.job_ID'), primary_key=True)
    applicant_status = db.Column(db.String(250))
    rank_number = db.Column(db.Integer)


    applicant = relationship("Applicant", back_populates="application")
    job_listing = relationship("Job_listing", back_populates="application")