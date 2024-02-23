import boto3
import logging
from botocore.exceptions import ClientError
import uuid
from flask import request, jsonify, make_response
from models.applicantModel import Applicant
import json
from flask import Blueprint
from __init__ import db

applicant_routes = Blueprint('applicant', __name__)

@applicant_routes.route('/new_applicant', methods=['POST'])
def new_applicant():
    data = request.get_json()
    print("=====HELLO==========")
    print(data)

    try:
        # Applicant schema
        new_record = Applicant(
            email = data['email'], 
            first_name = data['first_name'], 
            last_name = data['last_name'], 
            phone_number = data['phone_number'], 
            school = data['school'], 
            course_of_study = data['course_of_study'], 
            GPA = data['GPA'], 
            grad_month = data['grad_month'],
            past_salary = data['past_salary'],
            work_permit = data['work_permit']
        )

        db.session.add(new_record)
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
    print("========REACHED=========")
    aws_access_key_id = 'AKIAQ3EGVT4KGSPT4YKR'
    aws_secret_access_key = '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'
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    try:
        # File schema
        email = request.form.get('email')
        resume_file = request.files['resume']
        query_candidate = Applicant.query.get(email)
        # transcript_file = data['transcript']
        # reference_letter_file = data['reference_letter']

        new_filename = uuid.uuid4().hex + '.pdf'

        bucket_name = 'candidate-uploaded-files'

        s3_client.upload_fileobj(resume_file, bucket_name, new_filename)

        # db.session.commit()

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
