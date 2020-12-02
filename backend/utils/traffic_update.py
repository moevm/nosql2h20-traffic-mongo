import threading
import time
import random
from pymongo import UpdateOne
from pymongo.errors import BulkWriteError
from models.get_model import get_mongo, DB_NAME


def start_updating_thread():
    th = threading.Thread(target=update_data)
    th.start()
    return th


def update_data():
    time.sleep(60)
    mongo = get_mongo()
    db = mongo[DB_NAME]
    if mongo is None:
        print("Starting second thread failed")
        return None
    count = db.ways.count()
    print("Second thread started")
    while True:
        update_all_at_once(db.ways.find(), db)


def update_all_at_once(ways, db):
    try:
        update_el = [
            UpdateOne(
                {'_id': el['_id']},
                {'$set':
                     {'avg_speed': random.uniform(0, 100)}
                 }
            )
            for el in ways]
        result = db.ways.bulk_write(update_el)
        print(f"Values updated, errors: {result.bulk_api_result['writeErrors']}")
    except BulkWriteError as bwe:
        print(bwe.details)
    except BaseException:
        print("Unrecognized error")
    time.sleep(10 * 60)
