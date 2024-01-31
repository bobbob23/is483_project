from __init__ import db

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