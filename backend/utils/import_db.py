from models.get_model import get_mongo, DB_NAME
from pymongo import UpdateOne
from pymongo.errors import BulkWriteError
import json


def pls_import_collection(collection_name, data):
    db = get_mongo()[DB_NAME]
    collection = db.get_collection(collection_name)
    try:
        update_el = [
            UpdateOne(
                {'_id': el['_id']},
                {'$set':
                     el
                 },
                upsert=True
            )
            for el in data]
        result = collection.bulk_write(update_el)
        print(f"Values updated, errors: {result.bulk_api_result}")
    except BulkWriteError as bwe:
        print(bwe.details)
        return str(bwe.details)
    except BaseException as err:
        print("Unrecognized error in import:\n {}".format(err))
        return "Unrecognized error in import:\n {}".format(err)
    return None


def read_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data
