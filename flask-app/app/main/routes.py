from flask import Blueprint, render_template, session, redirect, request
from flask import jsonify
from ..db.db import MockDatabase

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/get-data")
def get_data():
    return jsonify({"message": "This is dummy data", "status": "success"})


@main.route("/set-user/<username>")
def set_user(username):
    user_map = {"Alice": 1, "Bob": 2, "Claire": 3}
    session["user"] = username
    session["user_id"] = user_map.get(username)
    return redirect(request.referrer or "/")


@main.route("/dashboard")
def dashboard():
    current_user_id = session.get("user_id", 1)
    events = MockDatabase.get_all("event")
    users = MockDatabase.get_all("user")
    user_map = {user["id"]: user for user in users}

    # Attach user info to each event
    enriched_events = []
    for event in events:
        if event["user_id"] != current_user_id:
            user = user_map.get(event["user_id"], {})
            enriched_events.append(
                {
                    **event,
                    "username": user.get("username", "Unknown"),
                    "email": user.get("email", ""),
                    "avatar_url": event.get(
                        "avatar_url",
                        "https://api.dicebear.com/7.x/miniavs/svg?seed=User",
                    ),
                }
            )

    return render_template("main/dashboard.html", events=enriched_events)


@main.route("/time-slot")
def time_slot():
    return render_template("main/time_slot.html")


@main.route("/db-test")
def db_test():
    MockDatabase.insert("test_table", {"id": 1, "name": "Test"})
    MockDatabase.get_all("test_table")
    data = MockDatabase.get_all("test_table")
    return jsonify(data)


@main.route("/calendar")
def calendar():
    return render_template("main/calendar.html")
