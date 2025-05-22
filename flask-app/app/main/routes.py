from flask import Blueprint, render_template, session, redirect, request
from flask import jsonify
from ..db.db import MockDatabase

import random

RANDOM_NAMES = [
    "Alex",
    "Jamie",
    "Taylor",
    "Jordan",
    "Casey",
    "Riley",
    "Morgan",
    "Avery",
    "Quinn",
    "Sage",
    "River",
    "Phoenix",
    "Rowan",
    "Skylar",
    "Cameron",
    "Dakota",
    "Emery",
    "Finley",
    "Hayden",
    "Indigo",
    "Justice",
    "Kendall",
    "Logan",
    "Marley",
]


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
        accepted_by = event.get("accepted_by")
        if event["user_id"] != current_user_id and (
            accepted_by is None or accepted_by == current_user_id
        ):
            user = user_map.get(event["user_id"], {})
            username = user.get("username", random.choice(RANDOM_NAMES))
            email = user.get("email", f"{username.lower()}@example.com")
            enriched_events.append(
                {
                    **event,
                    "username": username,
                    "email": email,
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
    current_user_id = session.get("user_id", 1)
    calendar_entries = MockDatabase.get_all("calendar")
    events = MockDatabase.get_all("event")
    users = MockDatabase.get_all("user")
    user_map = {user["id"]: user for user in users}
    event_map = {event["id"]: event for event in events}

    # Filter calendar entries for current user and enrich with event/user info
    enriched_calendar = []
    for entry in calendar_entries:
        if entry["accept_id"] == current_user_id:
            event = event_map.get(entry["event_id"])
            if event:
                owner = user_map.get(event["user_id"], {})
                enriched_calendar.append(
                    {
                        "event_title": event.get("event_title"),
                        "event_description": event.get("event_description"),
                        "start_time": event.get("start_time"),
                        "end_time": event.get("end_time"),
                        "event_location": event.get("event_location"),
                        "event_additional_notes": event.get("event_additional_notes"),
                        "owner_name": owner.get("username", "Unknown"),
                        "owner_email": owner.get("email", ""),
                        "avatar_url": owner.get(
                            "avatar_url",
                            "https://api.dicebear.com/7.x/miniavs/svg?seed=User",
                        ),
                    }
                )

    return render_template("main/calendar.html", calendar=enriched_calendar)
