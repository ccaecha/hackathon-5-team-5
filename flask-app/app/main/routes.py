from flask import Blueprint, render_template
from flask import jsonify
from ..db.db import MockDatabase

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/get-data")
def get_data():
    return jsonify({"message": "This is dummy data", "status": "success"})


@main.route("/dashboard")
def dashboard():
    return render_template("main/dashboard.html")


@main.route("/db-test")
def db_test():
    MockDatabase.insert("test_table", {"id": 1, "name": "Test"})
    MockDatabase.get_all("test_table")
    data = MockDatabase.get_all("test_table")
    return jsonify(data)
