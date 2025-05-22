from flask import Blueprint, render_template, session
from flask import jsonify
from ..db.db import MockDatabase

blueprint = Blueprint("backend", __name__)


# @blueprint.route("/get-data", methods=["GET"])
# def get_data(table, id):
#     data = MockDatabase.find(table, lambda x: x["id"] == id)
#     return jsonify(data[0] if data else None)

# @blueprint.route("/insert-data", methods=["POST"])
# def insert_data(table, record):
#     MockDatabase.insert(table, record)
#     return jsonify({"status": "success", "message": "Data inserted successfully"})


@blueprint.route("/event", methods=["GET"])
def get_event(id):
    data = MockDatabase.find("event", lambda x: x["id"] == id)
    return jsonify(data[0] if data else None)


@blueprint.route("/event", methods=["POST"])
def insert_event(record):
    MockDatabase.insert("event", record)
    return jsonify({"status": "success", "message": "Event inserted successfully"})


@blueprint.route("/event", methods=["PUT"])
def update_event(id, record):
    updated_count = MockDatabase.update(
        "event", lambda x: x["id"] == id, lambda x: {**x, **record}
    )
    return jsonify(
        {
            "status": "success",
            "message": f"{updated_count} event(s) updated successfully",
        }
    )


@blueprint.route("/event", methods=["DELETE"])
def delete_event(id):
    deleted_count = MockDatabase.delete("event", lambda x: x["id"] == id)
    return jsonify(
        {
            "status": "success",
            "message": f"{deleted_count} event(s) deleted successfully",
        }
    )


@blueprint.route("/user", methods=["GET"])
def get_user(id):
    data = MockDatabase.find("user", lambda x: x["id"] == id)
    return jsonify(data[0] if data else None)


@blueprint.route("/user", methods=["POST"])
def insert_user(record):
    MockDatabase.insert("user", record)
    return jsonify({"status": "success", "message": "User inserted successfully"})


@blueprint.route("/user", methods=["PUT"])
def update_user(id, record):
    updated_count = MockDatabase.update(
        "user", lambda x: x["id"] == id, lambda x: {**x, **record}
    )
    return jsonify(
        {
            "status": "success",
            "message": f"{updated_count} user(s) updated successfully",
        }
    )


@blueprint.route("/user", methods=["DELETE"])
def delete_user(id):
    deleted_count = MockDatabase.delete("user", lambda x: x["id"] == id)
    return jsonify(
        {
            "status": "success",
            "message": f"{deleted_count} user(s) deleted successfully",
        }
    )


@blueprint.route("/calendar", methods=["GET"])
def get_calendar(id):
    data = MockDatabase.find("calendar", lambda x: x["id"] == id)
    return jsonify(data[0] if data else None)


@blueprint.route("/calendar", methods=["POST"])
def insert_calendar(record):
    MockDatabase.insert("calendar", record)
    return jsonify({"status": "success", "message": "Calendar inserted successfully"})


@blueprint.route("/calendar", methods=["PUT"])
def update_calendar(id, record):
    updated_count = MockDatabase.update(
        "calendar", lambda x: x["id"] == id, lambda x: {**x, **record}
    )
    return jsonify(
        {
            "status": "success",
            "message": f"{updated_count} calendar(s) updated successfully",
        }
    )


@blueprint.route("/calendar", methods=["DELETE"])
def delete_calendar(id):
    deleted_count = MockDatabase.delete("calendar", lambda x: x["id"] == id)
    return jsonify(
        {
            "status": "success",
            "message": f"{deleted_count} calendar(s) deleted successfully",
        }
    )
