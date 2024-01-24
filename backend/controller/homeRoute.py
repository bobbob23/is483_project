from flask import Blueprint

homes = Blueprint('homes', __name__)

@homes.route('/')
def home():
    return("<h2>Test</h2>")