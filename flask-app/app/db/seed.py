from datetime import datetime, timedelta
from .db import MockDatabase


def insert_fake_events():
    if not MockDatabase.get_all("event"):
        MockDatabase.insert(
            "event",
            {
                "user_id": 1,
                "event_title": "Math Tutoring",
                "event_description": "Help with calculus homework",
                "start_time": datetime.now(),
                "end_time": datetime.now() + timedelta(hours=2),
                "event_location": "Library",
                "event_additional_notes": "Bring your textbook",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User1",
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 2,
                "event_title": "Dog Walking",
                "event_description": "Walk my dog in the park",
                "start_time": datetime.now() + timedelta(days=1, hours=10),
                "end_time": datetime.now() + timedelta(days=1, hours=12),
                "event_location": "Coffee Shop",
                "event_additional_notes": "Dog is friendly",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User2",
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 3,
                "event_title": "Cat Sitting",
                "event_description": "Feed and play with my cat",
                "start_time": datetime.now() + timedelta(days=1, hours=10),
                "end_time": datetime.now() + timedelta(days=1, hours=12),
                "event_location": "Home",
                "event_additional_notes": "Cat is shy",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User3",
            },
        )


def insert_fake_users():
    if not MockDatabase.get_all("user"):
        user_map = {"Alice": 1, "Bob": 2, "Claire": 3}
        MockDatabase.insert(
            "user",
            {"id": user_map["Alice"], "username": "Alice", "email": "alice@email.com"},
        )
        MockDatabase.insert(
            "user", {"id": user_map["Bob"], "username": "Bob", "email": "bob@email.com"}
        )
        MockDatabase.insert(
            "user",
            {
                "id": user_map["Claire"],
                "username": "Claire",
                "email": "claire@email.com",
            },
        )
