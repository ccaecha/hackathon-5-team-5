from flask import Blueprint, render_template
from flask import jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/get-data')
def get_data():
    return jsonify({"message": "This is dummy data", "status": "success"})