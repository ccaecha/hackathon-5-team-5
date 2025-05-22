from flask import Blueprint, render_template
from flask import jsonify
from ..db.db import MockDatabase

blueprint = Blueprint("backend", __name__)

@blueprint.route("/get-data", methods=["GET"])
def get_data(table, id):
    data = MockDatabase.find(table, lambda x: x["id"] == id)
    return jsonify(data[0] if data else None)

@blueprint.route("/insert-data", methods=["POST"])
def insert_data(table, record):
    MockDatabase.insert(table, record)
    return jsonify({"status": "success", "message": "Data inserted successfully"})