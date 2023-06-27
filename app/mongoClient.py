import json
from pymongo import MongoClient

with open('../config.json') as config_file:
    config = json.load(config_file)

mongo_host = config['mongo_host']
mongo_port = config['mongo_port']
mongo_db_name = config['mongo_db_name']
mongo_collection_name = config['mongo_collection_name']
json_file_path = config['json_file_path']

class MongoClient:
    # Connect to MongoDB
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]