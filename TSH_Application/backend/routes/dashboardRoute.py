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
            

@dashboard_routes.route('/HR', methods=['GET'])
def get_GPA():
    try:
        query_applicant_listing = Applicant.query.all()
        gpa_dict = {'< 3.0': 0, '< 3.5': 0, '< 4.0': 0, '> 4.0': 0}
        school_dict = {}
        course_dict = {}
        past_salary_dict = {'< 3000': 0, '< 5000' : 0, '< 7000' : 0, '> 7000' : 0}
        permit_dict = {}
        data_list = {
            'GPA': gpa_dict,
            'School' : school_dict,
            'Courses' : course_dict,
            'Past_salary' : past_salary_dict,
            'Work_permit' : permit_dict
        
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
            'message': f'Consolidated GPA data is returned'
        })

    except Exception as e:
        return jsonify({
            'message': f'Failed to retrieve data!',
            'error' : str(e)
        })
