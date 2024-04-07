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
        
        # response_data = response_data = {"data":{"profile":{"basics":{"first_name":"John","last_name":"Ape","gender":"male","emails":["test1@hotmail.com"],"urls":["linkedin.com/in/test1"],"phone_numbers":["+65 1234 5678"],"date_of_birth":{"year":"null","month":"null","day":"null"},"address":"","total_experience_in_years":5,"profession":"Intern","summary":"","skills":["Python","HTML","CSS","PHP","JavaScript","MySQL","Firebase","Vue.js","Bootstrap","Pandas","Tableau","Matplotlib","Seaborn"],"has_driving_license":"false"},"languages":[{"name":"English","iso_code":"en","fluency":5},{"name":"Chinese","iso_code":"zh","fluency":5}],"educations":[{"start_year":2021,"is_current":"false","end_year":2025,"issuing_organization":"Singapore Management University (SMU)","description":"Bachelor of Science (Information Systems) - Business Analytics Track"}],"trainings_and_certifications":[{"year":"null","issuing_organization":"","description":"Heicoders Academy: AI100 Python Programming and Data Visualisation"}],"professional_experiences":[{"start_date":{"year":2020,"month":7},"is_current":"false","end_date":{"year":2023,"month":9},"duration_in_months":39,"company":"Accenture","location":"","title":"Backend Developer Intern","description":"Developed RESTful API endpoints using Java and the Spring Boot framework.\nContributed to regular code reviews, providing constructive feedback to peers, and actively participating in discussions to improve code quality and maintainability."},{"start_date":{"year":2023,"month":5},"is_current":"false","end_date":{"year":2024,"month":7},"duration_in_months":14,"company":"Accenture","location":"","title":"Business Analyst Intern","description":"Collaborated with the team to facilitate CR (Change Request) deliveries and streamline operations.\nEnhanced testing processes by developing an automated test script (Python, Selenium) utilized for shakedowns and regression testing.\nAssisted in the analysis and documentation of test results, contributing to improved communication and transparency within the team.\nGained hands-on experience in software development lifecycle, quality assurance, and agile methodologies."}, {"start_date":{"year":2023,"month":5},"is_current":"false","end_date":{"year":2024,"month":7},"duration_in_months":14,"company":"Google","location":"","title":"Business Analyst Intern","description":"Collaborated with the team to facilitate CR (Change Request) deliveries and streamline operations.\nEnhanced testing processes by developing an automated test script (Python, Selenium) utilized for shakedowns and regression testing.\nAssisted in the analysis and documentation of test results, contributing to improved communication and transparency within the team.\nGained hands-on experience in software development lifecycle, quality assurance, and agile methodologies."}, {"start_date":{"year":2023,"month":5},"is_current":"false","end_date":{"year":2024,"month":7},"duration_in_months":14,"company":"Microsoft","location":"","title":"Business Analyst Intern","description":"Collaborated with the team to facilitate CR (Change Request) deliveries and streamline operations.\nEnhanced testing processes by developing an automated test script (Python, Selenium) utilized for shakedowns and regression testing.\nAssisted in the analysis and documentation of test results, contributing to improved communication and transparency within the team.\nGained hands-on experience in software development lifecycle, quality assurance, and agile methodologies."}],"awards":[],"references":[]},"cv_text":"John Ape +65 1234 5678 | test1@hotmail.com | linkedin.com/in/test1 Internship availability: May 2023 - Aug 2023\nEDUCATION\nSingapore Management University (SMU) Bachelor of Science (Information Systems)\nAug 2021 - May 2025 (Expected)\n• Business Analytics Track\nPROJECT EXPERIENCES\nHDB Resale Price Analysis | Github\nTechnology: Python, Jupyter Notebook, Pandas, Numpy, Matplotlib, Seaborn\n• Conducted exploratory data analysis to understand the relationships between various factors and HDB resale prices, such as location, flat type, and lease remaining\n• Developed a linear regression model to predict future prices based on these factors\nUmbrelify| Umbrelify Technology: HTML, CSS, Javascript, Bootstrap, Vue.js, Firebase APIs: Google Maps, 24-hour Weather Forecast\n• Constructed a web application that provides users with advice on whether to bring an umbrella based on the weather forecast for their target location and time\n• Guided the team, established direction, organised team project environment, and achieved successful deployment\nOectopus| Github\n-\nTechnology: Figma\n• Built a mobile app prototype to deliver a platform for early childhood tutors to gain inspirations for dramatic corners ideas\n• Carried out A/B Testing to compare variations A and B in terms of ease of use ratings, with sample size of 20 participants, found that Variation A was perceived to be easier to use compared to Variation B\nSKILLS\nProgramming: Python, HTML, CSS, PHP, JavaScript Databases: MySQL, Firebase Certifications: Heicoders Academy: AI100 Python Programming and Data Visualisation Libraries/Frameworks: Vue.js, Bootstrap, Pandas Experience with Tableau, Matplotlib, Seaborn Languages: English, Chinese\nCO-CURRICULAR ACTIVITIES\nSMU Business Intelligence & Analytics Club Member\n• Attended workshops on NumPy, Matplotlib\nJan 2021 - Present","cv_language":"en"}}
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