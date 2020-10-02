from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db["test_collection"]
print("Before writing to bd: {}".format(collection.find_one()))
collection.save({"id": 0, "str": "Hello World!"})
print(collection.find_one())
print("After writing to bd: {}".format(collection.find_one()))
