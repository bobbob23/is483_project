from __init__ import db
from sqlalchemy.orm import relationship
from models.jobApplicationModel import Job_Application

class Applicant(db.Model):
    __tablename__ = 'Applicant'
    email = db.Column(db.String(150), primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.Integer)
    school = db.Column(db.String(150))
    course_of_study = db.Column(db.String(150))
    GPA = db.Column(db.String(20))
    grad_month = db.Column(db.DateTime(timezone=True))
    past_salary = db.Column(db.String(150))
    work_permit = db.Column(db.String(150))
    resume = db.Column(db.String(250))
    transcript = db.Column(db.String(250))
    reference_letter = db.Column(db.String(250))
    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))

    application = relationship("Job_Application", back_populates="applicant")