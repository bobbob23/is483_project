from flask import request, jsonify, make_response
from models.applicantModel import Applicant
import json
from flask import Blueprint
from __init__ import db

applicant_routes = Blueprint('applicant', __name__)

@applicant_routes.route('/new_applicant', methods=['POST'])
def new_applicant():
    data = request.get_json()

    try:
        new_record = Applicant(
            email = data['email'], 
            first_name = data['first_name'], 
            last_name = data['last_name'], 
            phone_number = data['phone_number'], 
            school = data['school'], 
            course_of_study = data['course_of_study'], 
            GPA = data['GPA'], 
            grad_month = data['grad_month']
        )

        db.session.add(new_record)
        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': 'Application has been received!'
        })

    except:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive application!'
        })
