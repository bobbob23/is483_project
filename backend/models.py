from .controller import db

class Applicant(db.Model):
    __tablename__ = 'Applicant'
    email = db.Column(db.String(150), primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = first_name = db.Column(db.String(150))
    GPA = db.Column(db.String(150))
    course_of_study = db.Column(db.String(150))
    month_grad = db.Column(db.DateTime(timezone=True))
