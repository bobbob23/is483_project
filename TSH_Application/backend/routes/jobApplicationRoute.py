from flask import request, jsonify, make_response
from models.applicantModel import Applicant
from models.jobListingModel import Job_listing
from models.jobApplicationModel import Job_Application
import json
from flask import Blueprint
from __init__ import db

job_application_routes = Blueprint('job_application', __name__)

@job_application_routes.route('/all_applicants', methods=['GET'])
def get_all_applicants_by_job_ID(job_ID=1):
    
    try:
        listing_query_list = Job_Application.query.all()
        queried_list = []
        applicant_list = []

        for row in listing_query_list:
            if row.job_ID == job_ID:
                queried_list.append(row)

        for applicant in queried_list:
            applicant_dict = {}
            applicant_dict['email'] = applicant.email
            applicant_dict['job_ID'] = applicant.job_ID
            applicant_dict['applicant_status'] = applicant.applicant_status
            applicant_dict['rank_number'] = applicant.rank_number
            applicant_dict['phone_number'] = Applicant.query.get(applicant_dict['email']).phone_number
            applicant_dict['grad_month'] = Applicant.query.get(applicant_dict['email']).grad_month
            applicant_list.append(applicant_dict)

        sorted_applicant_list = sorted(applicant_list, key=lambda x: x["rank_number"])

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": sorted_applicant_list,
            "applicant_num": len(applicant_list)
        })

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants for the job_ID!',
            'error' : str(e)
        })
    
@job_application_routes.route('/applicant_details', methods=['GET'])
def get_applicant_details(email='ryan@water.com', job_ID=1):
    
    try:
        queried_applicant = Job_Application.query.get((email, job_ID))

        applicant_dict = {}
        applicant_dict['email'] = email
        applicant_dict['first_name'] = Applicant.query.get(applicant_dict['email']).first_name
        applicant_dict['last_name'] = Applicant.query.get(applicant_dict['email']).last_name
        applicant_dict['phone_number'] = Applicant.query.get(applicant_dict['email']).phone_number
        applicant_dict['school'] = Applicant.query.get(applicant_dict['email']).school
        applicant_dict['course_of_study'] = Applicant.query.get(applicant_dict['email']).course_of_study
        applicant_dict['grad_month'] = Applicant.query.get(applicant_dict['email']).grad_month
        applicant_dict['GPA'] = Applicant.query.get(applicant_dict['email']).GPA
        

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": applicant_dict
        })

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants details for the job_ID!',
            'error' : str(e)
        })
    
@job_application_routes.route('/edit_applicant_status', methods=['PUT'])
def edit_applicant_status(email='ryan@water.com', job_ID=1, status="Reject"):

    try:
        queried_job_applicant = Job_Application.query.get((email, job_ID))
        queried_job_applicant.applicant_status = status

        db.session.commit()


        return jsonify({
            'isEdited': True,
            'message': f'Applicant ({email}) status for Job id ({job_ID}) has been edited!'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'isEdited': True,
            'message': f'Falied to edit Applicant ({email}) status for Job id ({job_ID})!',
            'error' : str(e)
        })
    