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
    current_user = session.get("user", "Alice")
    slots = [
        {
            "user_name": "Alice",
            "email": "alice@email.com",
            "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User1",
            "time": "Today, 2:00 PM - 4:00 PM",
            "location": "Library",
            "task": "Math Tutoring",
        },
        {
            "user_name": "Bob",
            "email": "bob@email.com",
            "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User2",
            "time": "Tomorrow, 10:00 AM - 12:00 PM",
            "location": "Coffee Shop",
            "task": "Dog Walking",
        },
        {
            "user_name": "Claire",
            "email": "claire@email.com",
            "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User3",
            "time": "Tomorrow, 10:00 AM - 12:00 PM",
            "location": "Home",
            "task": "Cat Sitting",
        },
    ]

    filtered_slots = [
        slot for slot in slots if slot["user_name"].lower() != current_user.lower()
    ]
    slots = filtered_slots
    # In production, you would fetch from the database:
    # slots = MockDatabase.get_all("slots")
    return render_template("main/dashboard.html", slots=slots)


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
