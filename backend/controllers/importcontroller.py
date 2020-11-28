from utils.import_db import pls_import_collection, read_json


def import_collection(c_name, file):
    data = read_json(file)
    return pls_import_collection(c_name, data)
