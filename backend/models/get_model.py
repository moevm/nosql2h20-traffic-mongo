from pymongo import MongoClient

MONGO_ENGINE = None
DB_NAME = 'map_spb'


def get_mongo():
    global MONGO_ENGINE
    if MONGO_ENGINE is None:
        MONGO_ENGINE = MongoClient('nosql2h20trafficmongo_mongo_1', 27017)
    return MONGO_ENGINE