import traceback
from flask import request, jsonify, make_response
from models.applicantModel import Applicant
from models.jobListingModel import Job_listing
from models.jobApplicationModel import Job_Application
from models.probabilityModel import Probability
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
            applicant_dict['phone_number'] = Applicant.query.get(applicant_dict['email']).phone_number
            applicant_dict['grad_month'] = Applicant.query.get(applicant_dict['email']).grad_month
            applicant_dict['first_name'] = Applicant.query.get(applicant_dict['email']).first_name
            applicant_dict['last_name'] = Applicant.query.get(applicant_dict['email']).last_name
            applicant_dict['school'] = Applicant.query.get(applicant_dict['email']).school
            applicant_dict['course_of_study'] = Applicant.query.get(applicant_dict['email']).course_of_study
            applicant_dict['GPA'] = Applicant.query.get(applicant_dict['email']).GPA
            applicant_dict['Skills'] = applicant.skill
            applicant_dict['rank_probability'] = round(Probability.query.get(applicant.email).overall_probability, 2)
            applicant_dict['past_salary'] = applicant.past_salary
            applicant_dict['work_permit'] = applicant.work_permit
            applicant_dict['start_date'] = applicant.start_date
            applicant_dict['end_date'] = applicant.end_date

            applicant_list.append(applicant_dict)
        

        sorted_applicant_list = sorted(applicant_list, key=lambda x: x["rank_probability"], reverse=True)
        print(sorted_applicant_list)

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": sorted_applicant_list,
            "applicant_num": len(applicant_list)
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants for the job_ID!',
            'error' : str(e)
        })
    
@job_application_routes.route('/applicant_details/<string:email>/<int:job_id>', methods=['GET'])
def get_applicant_details(email, job_id):
    
    try:
        queried_applicant = Job_Application.query.get((email, job_id))

        applicant_dict = {}
        applicant_dict['email'] = email
        applicant_dict['first_name'] = Applicant.query.get(applicant_dict['email']).first_name
        applicant_dict['last_name'] = Applicant.query.get(applicant_dict['email']).last_name
        applicant_dict['phone_number'] = Applicant.query.get(applicant_dict['email']).phone_number
        applicant_dict['school'] = Applicant.query.get(applicant_dict['email']).school
        applicant_dict['course_of_study'] = Applicant.query.get(applicant_dict['email']).course_of_study
        applicant_dict['grad_month'] = Applicant.query.get(applicant_dict['email']).grad_month
        applicant_dict['GPA'] = Applicant.query.get(applicant_dict['email']).GPA
        applicant_dict['skill'] = queried_applicant.skill
        applicant_dict['status'] = queried_applicant.applicant_status
        applicant_dict['reject_reason'] = queried_applicant.reject_reason
        

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
        
        unprocessed_list.reverse()

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
def edit_applicant_status(email, job_ID, status):

    try:
        queried_job_applicant = Job_Application.query.get((email, job_ID))
        current_status = queried_job_applicant.applicant_status
        query_job_listing = Job_listing.query.get(job_ID)

        # same status update
        if current_status == status:
            return jsonify({
                'isEdited': False,
                'message': f'Applicant ({email}) current status is {status}!'
            }) 
                            
        current_status_num_str = current_status.lower() + '_num'
        job_current_status_num = getattr(query_job_listing, current_status_num_str)
        new_current_num = int(job_current_status_num) - 1
        setattr(query_job_listing, current_status_num_str, str(new_current_num))

        new_status_num_str = status.lower() + '_num'
        job_new_status_num = getattr(query_job_listing, new_status_num_str)
        new_num = int(job_new_status_num) + 1
        setattr(query_job_listing, new_status_num_str, str(new_num))

        if status == "Reject":
            data = request.get_json()
            queried_job_applicant.reject_reason = data['reject_reason']

        queried_job_applicant.applicant_status = status
        db.session.commit()

        return jsonify({
            'isEdited': True,
            'message': f'Applicant ({email}) status for Job id ({job_ID}) has been edited!'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'isEdited': False,
            'message': f'Falied to edit Applicant ({email}) status for Job id ({job_ID})!',
            'error' : str(e)
        })

@job_application_routes.route('/score_details/<string:email>', methods=['GET'])
def get_applicant_score_details(email):
    
    try:
        queried_applicant = Probability.query.get(email)

        applicant_dict = {}
        applicant_dict['email'] = email
        applicant_dict['overall_probability'] = round(queried_applicant.overall_probability * 100, 2)
        applicant_dict['total_working_years'] = round(queried_applicant.total_working_years * 100, 2)
        applicant_dict['num_companies_worked'] = round(queried_applicant.num_companies_worked * 100, 2)
        applicant_dict['education_field'] = round(queried_applicant.education_field * 100, 2)
        applicant_dict['education_level'] = round(queried_applicant.education_level * 100, 2)   

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