from flask import request, jsonify, make_response
from models.applicantModel import Applicant
from models.jobListingModel import Job_listing
from models.jobApplicationModel import Job_Application
import json
from flask import Blueprint
from __init__ import db

job_application_routes = Blueprint('job_application', __name__)

@job_application_routes.route('/all_applicants/<int:job_ID>', methods=['GET'])
def get_all_applicants_by_job_ID(job_ID):
    
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
            applicant_dict['first_name'] = Applicant.query.get(applicant_dict['email']).first_name
            applicant_dict['last_name'] = Applicant.query.get(applicant_dict['email']).last_name
            applicant_dict['school'] = Applicant.query.get(applicant_dict['email']).school
            applicant_dict['course_of_study'] = Applicant.query.get(applicant_dict['email']).course_of_study
            applicant_dict['GPA'] = Applicant.query.get(applicant_dict['email']).GPA
            applicant_dict['past_salary'] = Applicant.query.get(applicant_dict['email']).past_salary
            applicant_dict['work_permit'] = Applicant.query.get(applicant_dict['email']).work_permit
            applicant_dict['start_date'] = Applicant.query.get(applicant_dict['email']).start_date
            applicant_dict['end_date'] = Applicant.query.get(applicant_dict['email']).end_date

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
    
@job_application_routes.route('/unprocessed_applicant_details', methods=['GET'])
def get_unprocessed_applicant_details():
    
    try:
        queried_applicant_list = Job_Application.query.all()
        unprocessed_list = []

        for applicant in queried_applicant_list:
            if (applicant.applicant_status == "Unprocessed"):
                applicant_dict = {}
                applicant_dict['email'] = applicant.email
                applicant_dict['first_name'] = Applicant.query.get(applicant_dict['email']).first_name
                applicant_dict['last_name'] = Applicant.query.get(applicant_dict['email']).last_name
                applicant_dict['phone_number'] = Applicant.query.get(applicant_dict['email']).phone_number
                applicant_dict['school'] = Applicant.query.get(applicant_dict['email']).school
                applicant_dict['course_of_study'] = Applicant.query.get(applicant_dict['email']).course_of_study
                applicant_dict['grad_month'] = Applicant.query.get(applicant_dict['email']).grad_month
                applicant_dict['GPA'] = Applicant.query.get(applicant_dict['email']).GPA

                unprocessed_list.append(applicant_dict)
            

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": unprocessed_list,
            "unprocessed_num": len(unprocessed_list)
        })

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants details for the job_ID!',
            'error' : str(e)
        })
    
@job_application_routes.route('/all_applicant_status', methods=['GET'])
def get_all_applicant_status():

    try:
        listing_query_list = Job_Application.query.all()
        unprocessed_num = 0
        reject_num = 0
        interview_num = 0
        shortlisted_num = 0

        for applicant in listing_query_list:
            if applicant.applicant_status == "Unprocessed":
                unprocessed_num += 1
            elif (applicant.applicant_status == "Reject"):
                reject_num += 1
            elif (applicant.applicant_status == "Interview"):
                interview_num += 1
            elif (applicant.applicant_status == "Shortlisted"):
                shortlisted_num += 1



        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "unprocessed": unprocessed_num,
            "reject": reject_num,
            "interview": interview_num,
            "shortlisted": shortlisted_num
        })

    except Exception as e:
        return jsonify({
            'message': f'Falied to retrieve data from database!',
            'error' : str(e)
        })
    
@job_application_routes.route('/edit_applicant_status/<string:email>/<int:job_ID>/<string:status>', methods=['PUT'])
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
    