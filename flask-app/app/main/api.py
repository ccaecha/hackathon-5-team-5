from flask import Blueprint, render_template, session, request, redirect, url_for
from flask import jsonify
from ..db.db import MockDatabase
from datetime import datetime

blueprint = Blueprint("backend", __name__)


@blueprint.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "error", "message": "Resource not found"}), 404


@blueprint.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"status": "error", "message": "Method not allowed"}), 405


@blueprint.route("/event/<id>", methods=["GET"])
def get_event(id):
    data = MockDatabase.find("event", lambda x: x["id"] == id)
    if len(data) == 0:
        return jsonify({"status": "error", "message": "Event not found"}), 404
    return jsonify({"status": "success", "data": data[0] if data else None})


@blueprint.route("/event", methods=["POST"])
def insert_event():
    start_time = request.form.get("start_time")
    start_date = request.form.get("start_date")
    datetime_str = f"{start_date} {start_time}"
    start_dt = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
    end_time = request.form.get("end_time")
    end_date = request.form.get("end_date")
    datetime_str = f"{end_date} {end_time}"
    end_dt = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
    record = {
        "user_id": request.form.get("user_id"),
        "event_title": request.form.get("event_title"),
        "event_description": request.form.get("event_description"),
        "start_time": start_dt,
        "end_time": end_dt,
        "event_location": request.form.get("event_location"),
        "event_additional_notes": request.form.get("event_additional_notes"),
        "accepted": False,
    }
    MockDatabase.insert("event", record)
    print(record)
    return redirect(url_for("main.dashboard"))

@blueprint.route("/event", methods=["GET"])
def get_all_events():
    data = MockDatabase.get_all("event")
    return jsonify({"status": "success", "data": data})


@blueprint.route("/event/<id>", methods=["PUT"])
def update_event(id):
    record = request.get_json()
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


@blueprint.route("/user/<id>", methods=["GET"])
def get_user(id):
    data = MockDatabase.find("user", lambda x: x["id"] == id)
    if len(data) == 0:
        return jsonify({"status": "error", "message": "User not found"}), 404
    return jsonify({"status": "success", "data": data[0] if data else None})


@blueprint.route("/user", methods=["GET"])
def get_all_users():
    data = MockDatabase.get_all("user")
    return jsonify({"status": "success", "data": data})


@blueprint.route("/user", methods=["POST"])
def insert_user():
    record = request.get_json()
    try:
        MockDatabase.insert("user", record)
        return jsonify({"status": "success", "message": "User inserted successfully"})
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@blueprint.route("/user/<id>", methods=["PUT"])
def update_user(id):
    record = request.get_json()
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


@blueprint.route("/calendar/<id>", methods=["GET"])
def get_calendar(id):
    data = MockDatabase.find("calendar", lambda x: x["id"] == id)
    if len(data) == 0:
        return jsonify({"status": "error", "message": "Calendar not found"}), 404
    return jsonify({"status": "success", "data": data[0] if data else None})


@blueprint.route("/calendar", methods=["GET"])
def get_all_calendars():
    data = MockDatabase.get_all("calendar")
    return jsonify({"status": "success", "data": data})


@blueprint.route("/calendar", methods=["POST"])
def insert_calendar():
    record = request.get_json()
    try:
        MockDatabase.insert("calendar", record)
        return jsonify(
            {"status": "success", "message": "Calendar inserted successfully"}
        )
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@blueprint.route("/calendar/<id>", methods=["PUT"])
def update_calendar(id):
    record = request.get_json()
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
