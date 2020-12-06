import threading
import time
import random
import numpy as np
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

type_rangom = [True]
def super_random():
    if type_rangom[0]:
        a = random.uniform(0, 100)
        b = np.random.normal(a, 50, 1)[0]
        if b < 0:
            b = 100 + b
        return b
    return np.random.poisson(lam=10) * 100


def update_all_at_once(ways, db):
    try:
        print('TYPE : ', type_rangom)
        update_el = [
            UpdateOne(
                {'_id': el['_id']},
                {'$set':
                     {'avg_speed': super_random() % 100}
                 }
            )
            for el in ways]
        type_rangom[0] = not type_rangom[0]
        result = db.ways.bulk_write(update_el)
        print(f"Values updated, errors: {result.bulk_api_result['writeErrors']}")
    except BulkWriteError as bwe:
        print(bwe.details)
    except BaseException as e:
        print("Unrecognized error", e)
    time.sleep(1 * 30)
