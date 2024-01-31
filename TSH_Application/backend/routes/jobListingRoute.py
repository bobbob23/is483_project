from flask import request, jsonify, make_response
from models.jobListingModel import Job_listing
import json
from flask import Blueprint
from __init__ import db

job_listing_routes = Blueprint('job_listing', __name__)

@job_listing_routes.route('/job_listings', methods=['GET'])
def get_job_listings():
    listing_query_list = Job_listing.query.all()
    job_list = []
    
    for job in listing_query_list:
        job_dict = {}
        job_dict['job_ID'] = job.job_ID
        job_dict['title'] = job.title
        job_dict['location'] = job.location
        job_dict['type'] = job.type
        job_dict['category'] = job.category
        job_dict['closing_date'] = job.closing_date
        job_list.append(job_dict)

    if len(job_list) != 0:
        return jsonify({
            "message": "Succesfully retrieved data from database!",
            "data": job_list
        })

    return ({
        "message": f"No data in database"
    })