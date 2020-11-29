from utils.import_db import pls_import_collection, read_json


def import_collection(c_name, data):
    try:
        data = read_json(data)
        return pls_import_collection(c_name, data)
    except BaseException as e:
        print('Json import error: {}'.format(e))
        return {'error': 'Json import error: {}'.format(e)}
