from flask import request, jsonify
from models.applicantModel import Applicant
from models.jobApplicationModel import Job_Application
from models.jobListingModel import Job_listing
from flask import Blueprint
from __init__ import db

dashboard_routes = Blueprint('dashboard', __name__)

def field_sum(field, field_dict):
    if field not in field_dict:
        field_dict[field] = 1
    else:
        field_dict[field] += 1

def field_conditions(field, field_dict, con1, con2, con3):
    if (field < con1):
        field_dict[f'< {con1}'] += 1
    elif (field < con2):
        field_dict[f'< {con2}'] += 1
    elif (field < con3):
        field_dict[f'< {con3}'] += 1
    else:
        field_dict[f'> {con3}'] += 1

def applicant_details_con(filter_column, filter_value):
    query_job_listing = Job_listing.query.filter(getattr(Job_listing, filter_column) == filter_value).all()
    gpa_dict = {'< 3.0': 0, '< 3.5': 0, '< 4.0': 0, '> 4.0': 0}
    school_dict = {}
    course_dict = {}
    past_salary_dict = {'< 3000': 0, '< 5000' : 0, '< 7000' : 0, '> 7000' : 0}
    permit_dict = {}
    status_dict = {'unprocessed': 0, 'shortlisted': 0, 'interview': 0, 'hired': 0}
    data_list = {
        'GPA': gpa_dict,
        'school' : school_dict,
        'courses' : course_dict,
        'past_salary' : past_salary_dict,
        'work_permit' : permit_dict,
        'status' : status_dict
    }

    job_id_list = []

    for listing in query_job_listing:
        job_id_list.append(listing.job_ID)
        status_dict['unprocessed'] += int(listing.unprocessed_num)
        status_dict['shortlisted'] += int(listing.shortlisted_num)
        status_dict['interview'] += int(listing.interview_num)

    applicant_list = Job_Application.query.filter(Job_Application.job_ID.in_(job_id_list)).all()

    email_set = set() 
    email_list = []

    for applicant in applicant_list:
        email = Applicant.query.get(applicant.email)
        if email not in email_set:
            email_list.append(applicant.email)
            email_set.add(email)
    
    applicant_detail_list = Applicant.query.filter(Applicant.email.in_(email_list)).all()

    for applicant in applicant_detail_list:
        GPA = float(applicant.GPA.split("/")[0])
        school = applicant.school
        course = applicant.course_of_study
        past_salary = applicant.past_salary
        work_permit = applicant.work_permit

        field_conditions(GPA, gpa_dict, 3.0, 3.5, 4.0)
        if past_salary != '':
            past_salary = int(past_salary)
            field_conditions(past_salary, past_salary_dict, 3000, 5000, 7000)

        field_sum(school, school_dict)
        field_sum(course, course_dict)
        field_sum(work_permit, permit_dict)
    
    return data_list


@dashboard_routes.route('/HR', methods=['GET'])
def get_HR():
    try:
        query_applicant_listing = Applicant.query.all()
        gpa_dict = {'< 3.0': 0, '< 3.5': 0, '< 4.0': 0, '> 4.0': 0}
        school_dict = {}
        course_dict = {}
        past_salary_dict = {'< 3000': 0, '< 5000' : 0, '< 7000' : 0, '> 7000' : 0}
        permit_dict = {}
        data_list = {
            'GPA': gpa_dict,
            'school' : school_dict,
            'courses' : course_dict,
            'past_salary' : past_salary_dict,
            'work_permit' : permit_dict
        }

        for applicant in query_applicant_listing:
            GPA = float(applicant.GPA.split("/")[0])
            school = applicant.school
            course = applicant.course_of_study
            past_salary = applicant.past_salary
            work_permit = applicant.work_permit

            field_conditions(GPA, gpa_dict, 3.0, 3.5, 4.0)
            if past_salary != '':
                past_salary = int(past_salary)
                field_conditions(past_salary, past_salary_dict, 3000, 5000, 7000)

            field_sum(school, school_dict)
            field_sum(course, course_dict)
            field_sum(work_permit, permit_dict)

        return jsonify({
            'data': data_list,
            'message': f'Consolidated HR data is returned'
        })

    except Exception as e:
        return jsonify({
            'message': f'Failed to retrieve data!',
            'error' : str(e)
        })

@dashboard_routes.route('/manager/<specific_department>', methods=['GET'])
def dashboard_manager_department(specific_department):
    try:
        data_list = applicant_details_con('department', specific_department)
        return jsonify({
            'data': data_list,
            'message': f'Consolidated department data is returned'
        })

    except Exception as e:
        return jsonify({
            'message': f'Failed to retrieve data!',
            'error' : str(e)
        })

@dashboard_routes.route('/dashboard/<job_id>', methods=['GET'])
def dashboard_job_id(job_id):
    try:
        data_list = applicant_details_con('job_ID', job_id)
        return jsonify({
            'data': data_list,
            'message': f'Consolidated department data is returned'
        })

    except Exception as e:
        return jsonify({
            'message': f'Failed to retrieve data!',
            'error' : str(e)
        })