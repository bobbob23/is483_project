from __init__ import db

class Job_listing(db.Model):
    __tablename__ = 'Job_listing'
    job_ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    location = db.Column(db.String(150))
    type = db.Column(db.Integer)
    category = db.Column(db.String(150))
    closing_date = db.Column(db.DateTime(timezone=True))