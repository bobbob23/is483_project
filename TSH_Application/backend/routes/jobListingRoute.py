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

@job_listing_routes.route('/new_job_listing', methods=['POST'])
def new_job_listing():
    data = request.get_json()

    try:
        new_record = Job_listing(
            title = data['title'], 
            location = data['location'], 
            type = data['type'], 
            category = data['category'],
            closing_date = data['closing_date']
        )

        db.session.add(new_record)
        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': 'A new job listing has been saved!'
        })

    except Exception as e:
        return jsonify({
            'isApplied': False,
            'message': 'Failed to save job listing!',
            'error' : str(e)
        })
    
@job_listing_routes.route('/edit_job_listing', methods=['PUT'])
def edit_job_listing(job_id):
    edit_data = request.get_json()
    query_job_listing = Job_listing.query.get(job_id)

    try:
        query_job_listing.title = edit_data['title'], 
        query_job_listing.location = edit_data['location'], 
        query_job_listing.type = edit_data['type'], 
        query_job_listing.category = edit_data['category'],
        query_job_listing.closing_date = edit_data['closing_date']

        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': f'Job id {job_id} has been saved!'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'isApplied': False,
            'message': f'Failed to edit job id {job_id}!',
            'error' : str(e)
        })
    
@job_listing_routes.route('/delete_job_listing', methods=['DELETE'])
def delete_job_listing(job_id):
    query_job_listing = Job_listing.query.get(job_id)

    try:
        db.session.delete(query_job_listing)
        db.session.commit()

        return jsonify({
            'isApplied': True,
            'message': f'Job id {job_id} has been deleted!'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'isApplied': False,
            'message': f'Failed to delete job id {job_id}!',
            'error' : str(e)
        })