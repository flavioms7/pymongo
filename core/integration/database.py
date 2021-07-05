from pymongo import MongoClient


def record(entry):
    client = MongoClient('mongodb://localhost:27017/')
    database = client["person"]
    col = database["phone"]
    post_id = col.insert_one(entry).inserted_id

    return post_id
