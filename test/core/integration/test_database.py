import mongomock
from core.integration.database import record

def test_database():

    entry = {
        "name": "sample Name"
    }

    result = record(entry)

    assert result is not None






