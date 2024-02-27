from __init__ import db
from sqlalchemy.orm import relationship

class Job_listing(db.Model):
    __tablename__ = 'Job_listing'
    job_ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    location = db.Column(db.String(150))
    type = db.Column(db.Integer)
    department = db.Column(db.String(150))
    opening_date = db.Column(db.DateTime(timezone=True))
    closing_date = db.Column(db.DateTime(timezone=True))
    job_status = db.Column(db.String(150))
    hiring_manager = db.Column(db.String(150))
    salary = db.Column(db.String(150))
    job_description = db.Column(db.String(5000))
    job_requirement = db.Column(db.String(5000))
    work_permit = db.Column(db.JSON)
    unprocessed_num = db.Column(db.Integer)
    shortlisted_num = db.Column(db.Integer)
    interview_num = db.Column(db.Integer)

    application = relationship("Job_Application", back_populates="job_listing")