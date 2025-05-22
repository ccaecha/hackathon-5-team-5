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
                "accepted": False,
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
                "accepted": False,
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
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 4,
                "event_title": "House Cleaning",
                "event_description": "Deep clean kitchen and living room",
                "start_time": datetime.now() + timedelta(days=2, hours=14),
                "end_time": datetime.now() + timedelta(days=2, hours=18),
                "event_location": "Downtown Apartment",
                "event_additional_notes": "Cleaning supplies provided",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User4",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 5,
                "event_title": "Grocery Shopping",
                "event_description": "Weekly grocery run for elderly neighbor",
                "start_time": datetime.now() + timedelta(days=3, hours=9),
                "end_time": datetime.now() + timedelta(days=3, hours=11),
                "event_location": "Whole Foods Market",
                "event_additional_notes": "Shopping list and payment provided",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User5",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 6,
                "event_title": "Furniture Assembly",
                "event_description": "Help assemble IKEA bookshelf and desk",
                "start_time": datetime.now() + timedelta(days=1, hours=15),
                "end_time": datetime.now() + timedelta(days=1, hours=19),
                "event_location": "Student Dorm Room",
                "event_additional_notes": "Tools provided, pizza included!",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User6",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 7,
                "event_title": "Language Exchange",
                "event_description": "Practice Spanish conversation over coffee",
                "start_time": datetime.now() + timedelta(days=4, hours=16),
                "end_time": datetime.now() + timedelta(days=4, hours=18),
                "event_location": "Central Cafe",
                "event_additional_notes": "Beginner friendly, I'll buy the coffee",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User7",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 8,
                "event_title": "Plant Watering",
                "event_description": "Water indoor plants while I'm on vacation",
                "start_time": datetime.now() + timedelta(days=7, hours=12),
                "end_time": datetime.now() + timedelta(days=7, hours=13),
                "event_location": "Garden District Apartment",
                "event_additional_notes": "Instructions left on counter, spare key under mat",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User8",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 9,
                "event_title": "Computer Setup",
                "event_description": "Help set up new laptop and transfer files",
                "start_time": datetime.now() + timedelta(days=2, hours=19),
                "end_time": datetime.now() + timedelta(days=2, hours=22),
                "event_location": "Tech Support Cafe",
                "event_additional_notes": "Bring USB drive if possible",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User9",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 10,
                "event_title": "Moving Help",
                "event_description": "Help load/unload moving truck",
                "start_time": datetime.now() + timedelta(days=5, hours=8),
                "end_time": datetime.now() + timedelta(days=5, hours=14),
                "event_location": "Oak Street to Pine Avenue",
                "event_additional_notes": "Lunch and drinks provided, heavy lifting involved",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User10",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 11,
                "event_title": "Photography Session",
                "event_description": "Need photographer for small birthday party",
                "start_time": datetime.now() + timedelta(days=6, hours=17),
                "end_time": datetime.now() + timedelta(days=6, hours=20),
                "event_location": "Riverside Park Pavilion",
                "event_additional_notes": "Bring your own camera, will provide memory card",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User11",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 12,
                "event_title": "Yard Work",
                "event_description": "Rake leaves and trim bushes",
                "start_time": datetime.now() + timedelta(days=3, hours=13),
                "end_time": datetime.now() + timedelta(days=3, hours=17),
                "event_location": "Suburban Home",
                "event_additional_notes": "All tools provided, wear old clothes",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User12",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 13,
                "event_title": "Baking Help",
                "event_description": "Help bake cookies for school fundraiser",
                "start_time": datetime.now() + timedelta(days=4, hours=10),
                "end_time": datetime.now() + timedelta(days=4, hours=15),
                "event_location": "Home Kitchen",
                "event_additional_notes": "All ingredients provided, take some cookies home!",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User13",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 14,
                "event_title": "Airport Pickup",
                "event_description": "Pick up friend from airport",
                "start_time": datetime.now() + timedelta(days=8, hours=22),
                "end_time": datetime.now() + timedelta(days=9, hours=0),
                "event_location": "International Airport",
                "event_additional_notes": "Flight arrives at 10:30 PM, gas money provided",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User14",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 15,
                "event_title": "Study Group",
                "event_description": "Join chemistry study group before exam",
                "start_time": datetime.now() + timedelta(days=1, hours=18),
                "end_time": datetime.now() + timedelta(days=1, hours=21),
                "event_location": "University Library",
                "event_additional_notes": "Bring organic chemistry textbook",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User15",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 16,
                "event_title": "Baby Sitting",
                "event_description": "Watch 6-year-old for date night",
                "start_time": datetime.now() + timedelta(days=6, hours=19),
                "end_time": datetime.now() + timedelta(days=6, hours=23),
                "event_location": "Family Home",
                "event_additional_notes": "Kid-friendly, dinner already prepared",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User16",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 17,
                "event_title": "Painting Help",
                "event_description": "Help paint bedroom walls",
                "start_time": datetime.now() + timedelta(days=5, hours=9),
                "end_time": datetime.now() + timedelta(days=5, hours=16),
                "event_location": "Two-bedroom Apartment",
                "event_additional_notes": "Paint and supplies provided, order pizza for lunch",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User17",
                "accepted": False,
            },
        )
        MockDatabase.insert(
            "event",
            {
                "user_id": 18,
                "event_title": "Event Setup",
                "event_description": "Help set up tables and decorations for wedding",
                "start_time": datetime.now() + timedelta(days=9, hours=7),
                "end_time": datetime.now() + timedelta(days=9, hours=12),
                "event_location": "Community Center",
                "event_additional_notes": "Early morning setup, breakfast provided",
                "avatar_url": "https://api.dicebear.com/7.x/miniavs/svg?seed=User18",
                "accepted": False,
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
