import traceback
import requests
import base64
from flask import request, jsonify
from models.applicantModel import Applicant
from models.jobApplicationModel import Job_Application
from models.jobListingModel import Job_listing
from flask import Blueprint
from __init__ import db
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]

autofill_routes = Blueprint('autofill', __name__)

@autofill_routes.route('/autofill', methods=['POST'])
def get_autofill():    
    try:
        file = request.files['pdf_file']

        url = 'https://cvparser.ai/api/v3/parse'
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': API_KEY
        }

        encoded_file = base64.b64encode(file.read()).decode('utf-8')
        data = {
            'base64': encoded_file
        }
        
        response = requests.post(url, headers=headers, json=data)
        print(response.text)
        response_data = response.json()['data']
        print(response_data)

        return jsonify({
            'message': 'Succesfully retrieved data from database!',
            "data": response_data
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            'isApplied': False,
            'message': 'Failed to receive applicants details for the job_ID!',
            'error' : str(e)
        })