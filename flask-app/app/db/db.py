from datetime import datetime


class MockDatabase:
    _data = {}

    @classmethod
    def insert(cls, table, record, use_auto_id=True):
        if table not in cls._data:
            cls._data[table] = []
        if use_auto_id or "id" not in record:
            if isinstance(record, dict):
                record["id"] = len(cls._data[table]) + 1
        elif "id" in record:
            existing_ids = {r["id"] for r in cls._data[table]}
            if record["id"] in existing_ids:
                raise ValueError(f"ID {record['id']} already exists in table {table}")
        cls._data[table].append(record)

    @classmethod
    def get_all(cls, table):
        return cls._data.get(table, [])

    @classmethod
    def find(cls, table, predicate):
        return [record for record in cls._data.get(table, []) if predicate(record)]

    @classmethod
    def update(cls, table, predicate, update_fn):
        updated = 0
        for i, record in enumerate(cls._data.get(table, [])):
            if predicate(record):
                cls._data[table][i] = update_fn(record)
                updated += 1
        return updated

    @classmethod
    def delete(cls, table, predicate):
        original = len(cls._data.get(table, []))
        cls._data[table] = [
            record for record in cls._data.get(table, []) if not predicate(record)
        ]
        return original - len(cls._data[table])


# Example usage:
# To get all records from a table:
# records = MockDatabase.get_all("test_table")
# To insert a new record:
# MockDatabase.insert("test_table", {"id": 1, "name": "Test"})
# To find records that match a condition:
# records = MockDatabase.find("test_table", lambda x: x["id"] == 1)
# To update records that match a condition:
# updated_count = MockDatabase.update("test_table", lambda x: x["id"] == 1, lambda x: {**x, "name": "Updated"})
# To delete records that match a condition:
# deleted_count = MockDatabase.delete("test_table", lambda x: x["id"] == 1)
#
# Table structure:
# event_table = {
#     "id": int,
#     "user_id": int,
#     "event_title": str,
#     "event_description": str,
#     "start_time": datetime,
#     "end_time": datetime,
#     "event_location": str,
#     "event_description": str,
#     "event_additional_notes": str,
#     "accepted": bool
#     }
# calender_table = {
#     "send_id": int,
#     "accept_id": int,
#     "event_id": int,
# }
