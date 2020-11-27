from models.get_model import get_mongo, DB_NAME
import json
import os
from zipfile import ZipFile


def write_data_to_json(collection_name, path= './'):
    try:
        os.mkdir(path)
    except OSError:
        pass
    db = get_mongo()[DB_NAME]
    collection = db.get_collection(collection_name)
    doc_list = list(collection.find())
    filename = f'{path}/{collection_name}.json'
    with open(filename, 'w') as outfile:
        json.dump(doc_list, outfile, ensure_ascii=False)
    return filename


def export_collections():
    path = './'
    col_names = ['nodes', 'ways', 'relations']
    filenames = []
    for name in col_names:
        filename = write_data_to_json(name, path)
        filenames.append(filename)
    zip_name = 'database.zip'
    create_archive(zip_name, filenames)
    return zip_name


def create_archive(name, files):
    with ZipFile(name, 'w') as zipObj:
        for file in files:
            zipObj.write(file)
    print('Archive was created!')
