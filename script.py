import json
from pymongo import MongoClient


with open('config.json') as config_file:
    config = json.load(config_file)

mongo_host = config['mongo_host']
mongo_port = config['mongo_port']
mongo_db_name = config['mongo_db_name']
mongo_collection_name = config['mongo_collection_name']
json_file_path = config['json_file_path']

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db_name]
collection = db[mongo_collection_name]

# Load data from JSON file
with open(json_file_path) as file:
    data = json.load(file)

# Insert data into MongoDB collection
collection.insert_many(data)
print("Data Inserted")

# Create an index
index_keys = [ ('name', 1)]  
index_name = 'index_on_name'  
collection.create_index(index_keys, name=index_name)
print("Index Created")

# Close the MongoDB connection
client.close()

