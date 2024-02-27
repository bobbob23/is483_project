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
        closing_date = Job_listing.query.get(job_ID).closing_date
        queried_list = []
        applicant_list = []
        unprocessed_num = 0
        shortlisted_num = 0
        interview_num = 0

        for row in listing_query_list:
            if row.job_ID == job_ID:
                queried_list.append(row)

        for applicant in queried_list:
            applicant_dict = {}
            applicant_dict['email'] = applicant.email
            applicant_dict['job_ID'] = applicant.job_ID
            applicant_dict['applicant_status'] = applicant.applicant_status
            applicant_dict['rank_number'] = applicant.rank_number
            applicant_list.append(applicant_dict)

            if (applicant.applicant_status == "Unprocessed"):
                unprocessed_num += 1
            elif (applicant.applicant_status == "Shortlisted"):
                shortlisted_num += 1
            elif (applicant.applicant_status == "Interview"):
                interview_num += 1

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": applicant_list,
            "unprocessed_num" : unprocessed_num,
            "shortlisted_num": shortlisted_num,
            "interview_num": interview_num,
            "closing_date": closing_date
        })

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants for the job_ID!',
            'error' : str(e)
        })