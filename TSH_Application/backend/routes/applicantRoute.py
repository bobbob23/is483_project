from flask import request, jsonify, make_response
from models.applicantModel import Applicant
import json
from flask import Blueprint

applicant_routes = Blueprint('applicant', __name__)

@applicant_routes.route('/applicant')
def get_all_applicant():
    applicant_list = Applicant.query.all()
    for applicant in applicant_list:
        print(applicant.email)
        print(applicant.first_name)
        print(applicant.last_name)
        print(applicant.phone_number)
        print(applicant.school)
        print(applicant.course_of_study)
        print(applicant.GPA)
        print(applicant.grad_month)
    return "OKAY"