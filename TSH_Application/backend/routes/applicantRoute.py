import traceback
import boto3
import os
import logging
from services import file_services
from botocore.exceptions import ClientError
import uuid
from flask import request, jsonify
from models.applicantModel import Applicant
from models.jobApplicationModel import Job_Application
from models.jobListingModel import Job_listing
from flask import Blueprint
from __init__ import db
from dotenv import load_dotenv

applicant_routes = Blueprint('applicant', __name__)

load_dotenv()

ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["SECRET_ACCESS_KEY"]

@applicant_routes.route("/all_applicant_details", methods=["GET"])
def get_all_applicants():
      try:
        listing_query_list = Applicant.query.all()
        applicant_list = []
        for applicant in listing_query_list:
            applicant_dict = {}
            applicant_dict['email'] = applicant.email
            applicant_dict['fName'] = applicant.first_name
            applicant_dict['lName'] = applicant.last_name
            applicant_dict['number'] = applicant.phone_number
            applicant_dict['school'] = applicant.school
            applicant_dict['course'] = applicant.course_of_study
            applicant_dict['gpa'] = applicant.GPA
            applicant_dict['gradDate'] = applicant.grad_month
            applicant_dict['pastSalary'] = applicant.past_salary
            applicant_dict['workPermit'] = applicant.work_permit
            applicant_dict['startDate'] = applicant.start_date
            applicant_dict['endDate'] = applicant.end_date
            applicant_list.append(applicant_dict)
        
        applicant_list.reverse()
        
        return jsonify({
            'message': "Successfully retrieved data from database",
            "data": applicant_list
        })
      
      except Exception as e:
        return jsonify({
            'message': 'Failed to retrieve applicants!',
            'error' : str(e)
        })

@applicant_routes.route('/new_applicant', methods=['POST'])
def new_applicant():
    data = request.get_json()

    try:
        # Applicant schema
        new_record = Applicant(
            email = data['email'], 
            first_name = data['fName'], 
            last_name = data['lName'], 
            phone_number = data['number'], 
            school = data['school'], 
            course_of_study = data['course'], 
            GPA = data['gpa'], 
            grad_month = data['gradDate']
        )

        pastSalary = "0"

        if 'pastSalary' in data:
            pastSalary = data['pastSalary']

        new_job_application_record = Job_Application(
            email = data['email'],
            job_ID = data['job_id'],
            applicant_status = "Unprocessed",
            skill = ['PHP', 'Python'],
            rank_probability = None,
            past_salary = pastSalary,
            work_permit = data['workPermit'],
            start_date = data['startDate'],
            end_date = data['endDate']
        )

        query_job_listing = Job_listing.query.get(data['job_id'])
        query_job_listing.unprocessed_num += 1

        db.session.add(new_record)
        db.session.add(new_job_application_record)
        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': 'Application has been received!'
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive application!',
            'error' : str(e)
        })

@applicant_routes.route('/new_applicant_files', methods=['POST'])
def new_applicant_files():

    s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    resume_file = None
    transcript_file = None
    reference_letter_file = None

    try:
        # File schema
        email = request.form.get('email')
        job_id = request.form.get('job_id')
        if 'resume' in request.files:
            resume_file = request.files['resume']
        if 'transcript' in request.files:
            transcript_file = request.files['transcript']
        if 'reference_letter' in request.files:
            reference_letter_file = request.files['reference_letter']
        
        file_dict = dict(
            resume = resume_file,
            transcript = transcript_file,
            reference_letter = reference_letter_file
        )

        query_candidate = Job_Application.query.get((email, job_id))
        bucket_name = 'candidate-uploaded-files'

        for key, value in file_dict.items():
            if value is not None:
                folder_name = key
                new_filename = uuid.uuid4().hex + '.pdf'
                s3_client.upload_fileobj(value, bucket_name, f'{folder_name}/{new_filename}')
                setattr(query_candidate, folder_name, new_filename)

        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': 'Application has been received!'
        })
    
    except ClientError as e:
        print("========ERROR========")
        print(logging.error(e))

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive application!',
            'error' : str(e)
        })

@applicant_routes.route('/applicant_files/<string:email>/<int:job_id>', methods=['GET'])
def applicant_details(email, job_id):

    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_ACCESS_KEY
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # data directory, INPUT YOUR OWN PATH
    data_folder = r"applicantFiles"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    try:
        # File schema
        query_candidate = Job_Application.query.get((email, job_id))
        applicant_query = Applicant.query.get(email)
        fname = applicant_query.first_name
        lname = applicant_query.last_name
        resume_file = query_candidate.resume
        transcript_file = query_candidate.transcript
        reference_letter_file = query_candidate.reference_letter

        file_dict = dict(
            resume = resume_file,
            transcript = transcript_file,
            reference_letter = reference_letter_file
        )

        bucket_name = 'candidate-uploaded-files'
        
        for key, value in file_dict.items():
            folder_name = key
            file_uuid = value
            file_name = f"{fname}{lname}_{folder_name}.pdf"

            # subfolder_name = f'{fname}{lname}'
            # subfolder_path = os.path.join(data_folder, subfolder_name)

            # # Create the folder if it doesn't exist
            # if not os.path.exists(subfolder_path):
            #     os.makedirs(subfolder_path)
        
            folder_path = os.path.join(data_folder, file_name)
            s3_client.download_file(bucket_name, f"{folder_name}/{file_uuid}", Filename=folder_path)

        return jsonify({
            'isApplied': True,
            'message': 'Applicant details have been received!'
        })
    
    except ClientError as e:
        print("========ERROR========")
        print(logging.error(e))

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicant details!',
            'error' : str(e)
        })

# @applicant_routes.route('/process/<string:file>', methods=['GET'])
# def process(file):
#     return file_services.perform_parsing(file)

# @applicant_routes.route('/get_file', methods=['GET'])
# def get_file(key=""):
#     return file_services.fetch_file(key)