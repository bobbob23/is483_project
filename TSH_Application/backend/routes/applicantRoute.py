import boto3
import os
import logging
from botocore.exceptions import ClientError
import uuid
from flask import request, jsonify
from models.applicantModel import Applicant
from models.jobApplicationModel import Job_Application
from flask import Blueprint
from __init__ import db
from dotenv import load_dotenv

applicant_routes = Blueprint('applicant', __name__)

load_dotenv()

ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["SECRET_ACCESS_KEY"]

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
            grad_month = data['gradDate'],
            past_salary = data['pastSalary'],
            work_permit = data['workPermit'],
            start_date = data['startDate'],
            end_date = data['endDate']
        )

        new_job_application_record = Job_Application(
            email = data['email'],
            job_ID = data['job_id'],
            applicant_status = "Unprocessed",
            rank_number = None
        )

        db.session.add(new_record)
        db.session.add(new_job_application_record)
        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': 'Application has been received!'
        })

    except Exception as e:
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

        query_candidate = Applicant.query.get(email)
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
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive application!',
            'error' : str(e)
        })

@applicant_routes.route('/applicant_files', methods=['GET'])
def applicant_details(email='ryanteo.2021@scis.smu.edu.sg'):

    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_ACCESS_KEY
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # data directory, INPUT YOUR OWN PATH
    data_folder = r"C:\Users\ASUS\Desktop\is483_project\TSH_Application\data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    try:
        # File schema
        query_candidate = Applicant.query.get(email)
        fname = query_candidate.first_name
        lname = query_candidate.last_name
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
