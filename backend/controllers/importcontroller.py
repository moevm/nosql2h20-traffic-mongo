from utils.import_db import import_collection, read_json


def import_collection(c_name, file):
    data = read_json(file)
    return import_collection(c_name, data)