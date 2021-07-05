from core.integration.database import record


def build_entry():
    entry = {
        "name": "Flavio Miranda",
        "ddd": 81,
        "phone_number": 988776655
    }

    id_entry = record(entry)

    print(id_entry)
