from datetime import datetime
from flask import request, jsonify, make_response
from models.jobListingModel import Job_listing
import json
from flask import Blueprint
from __init__ import db

job_listing_routes = Blueprint('job_listing', __name__)

@job_listing_routes.route('/job_listing_list', methods=['GET'])
def get_job_listings():
    try:
        listing_query_list = Job_listing.query.all()
        job_list = []
        
        for job in listing_query_list:
            job_dict = {}
            job_dict['job_ID'] = job.job_ID
            job_dict['title'] = job.title
            job_dict['location'] = job.location
            job_dict['type'] = job.type
            job_dict['department'] = job.department
            job_dict['opening_date'] = job.opening_date
            job_dict['closing_date'] = job.closing_date
            job_dict['description'] = job.job_description
            job_dict['requirement'] = job.job_requirement
            job_dict['unprocessed_num'] = job.unprocessed_num
            job_dict['shortlisted_num'] = job.shortlisted_num
            job_dict['interview_num'] = job.interview_num
            job_dict['reject_num'] = job.reject_num
            job_dict['hired_num'] = job.hired_num

            job_list.append(job_dict)

        return jsonify({
            "message": "Succesfully retrieved data from database!",
            "data": job_list,
            "job_listing_num": len(job_list)
        })

    except Exception as e:
        return jsonify({
            "message": f"No data in database",
            "error": str(e)
        })

@job_listing_routes.route('/job_listing/<int:job_id>', methods=['GET'])
def get_job_listing(job_id):
    
    try:
        query_job_listing = Job_listing.query.get(job_id)

        if (query_job_listing != 'None'):
            job_dict = {}
            job_dict['title'] = query_job_listing.title
            job_dict['location'] = query_job_listing.location
            job_dict['type'] = query_job_listing.type
            job_dict['department'] = query_job_listing.department
            job_dict['opening_date'] = query_job_listing.opening_date
            job_dict['closing_date'] = query_job_listing.closing_date
            job_dict['description'] = query_job_listing.job_description
            job_dict['requirement'] = query_job_listing.job_requirement
            job_dict['job_status'] = query_job_listing.job_status
            job_dict['hiring_manager'] = query_job_listing.hiring_manager
            job_dict['salary'] = query_job_listing.salary
            job_dict['work_permit'] = query_job_listing.work_permit

            return jsonify({
                "message": "Succesfully retrieved data from database!",
                "data": job_dict
            })
    
    except Exception as e:
        return jsonify({
            "message": f'Failed to retrieve data from database!',
            "error": str(e)
        })

@job_listing_routes.route('/new_job_listing', methods=['POST'])
def new_job_listing():
    data = request.get_json()

    try:
        new_record = Job_listing(
            title = data['title'], 
            location = data['location'], 
            type = data['type'], 
            department = data['department'],
            opening_date = data['opening_date'],
            closing_date = data['closing_date'],
            job_status = data['job_status'],
            hiring_manager = data['hiring_manager'],
            salary = data['salary'],
            job_description = data['job_description'],
            job_requirement = data['job_requirement'],
            unprocessed_num = 0,
            shortlisted_num = 0,
            interview_num = 0,
            reject_num = 0,
            hired_num = 0,
            # NEED TO ENSURE WORK_PERMIT IS STORED AS JSON
            work_permit = data['work_permit']
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
    
@job_listing_routes.route('/edit_job_listing/<int:job_id>', methods=['PUT'])
def edit_job_listing(job_id):
    edit_data = request.get_json()
    query_job_listing = Job_listing.query.get(job_id)
    
    try:
        query_job_listing.title = edit_data['title']
        query_job_listing.location = edit_data['location']
        query_job_listing.type = edit_data['type']
        query_job_listing.department = edit_data['department']
        query_job_listing.closing_date = edit_data['closing_date']
        query_job_listing.opening_date = edit_data['opening_date']
        query_job_listing.job_status = edit_data['job_status']
        query_job_listing.hiring_manager = edit_data['hiring_manager']
        query_job_listing.salary = edit_data['salary']
        query_job_listing.job_description = edit_data['description']
        query_job_listing.job_requirement = edit_data['requirement']
        query_job_listing.work_permit = edit_data['work_permit']

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
    
@job_listing_routes.route('/delete_job_listing/<int:job_id>', methods=['DELETE'])
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
    
@job_listing_routes.route('/active_job_listing_list', methods=['GET'])
def get_active_job_listings():
    
    try:
        listing_query_list = Job_listing.query.all()
        current_time = datetime.now()
        job_list = []
        
        for job in listing_query_list:
            job_dict = {}
            if (current_time < job.closing_date):
                job_dict['job_ID'] = job.job_ID
                job_dict['title'] = job.title
                job_dict['location'] = job.location
                job_dict['type'] = job.type
                job_dict['department'] = job.department
                job_dict['opening_date'] = job.opening_date
                job_dict['closing_date'] = job.closing_date
                job_dict['description'] = job.job_description
                job_dict['requirement'] = job.job_requirement
                job_dict['unprocessed_num'] = job.unprocessed_num
                job_dict['shortlisted_num'] = job.shortlisted_num
                job_dict['interview_num'] = job.interview_num
                job_dict['reject_num'] = job.reject_num
                job_dict['hired_num'] = job.hired_num

                job_list.append(job_dict)

        return jsonify({
            "message": "Succesfully retrieved data from database!",
            "data": job_list,
            "job_listing_num": len(job_list)
        })
    
    except Exception as e:
        return jsonify({
            'message': f"No data in database",
            'error' : str(e)
            })