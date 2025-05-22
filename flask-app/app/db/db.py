class MockDatabase:
    _data = {}

    @classmethod
    def insert(cls, table, record):
        if table not in cls._data:
            cls._data[table] = []
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
        cls._data[table] = [record for record in cls._data.get(table, []) if not predicate(record)]
        return original - len(cls._data[table])