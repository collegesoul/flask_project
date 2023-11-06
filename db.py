import os
import dotenv
from pymongo import MongoClient
from errors import KeyNotFound, KeyExists

# Load env files if there's one
dotenv.load_dotenv(dotenv.find_dotenv())

# Get mongodb user information
user = os.environ.get('MONGODB_USERNAME')
password = os.environ.get('MONGODB_PASSWORD')
host = os.environ.get('MONGODB_HOSTNAME')

# Get environment variables for database
connection = f"mongodb://{user}:{password}@{host}:27017/admin"

# Connect to mongodb client
client = MongoClient(connection)

# Access database and collection if it exists else creates it
database = client.keyvalues
collection = database.keyvaluepair


def get_keys() -> list:
    """get_keys function gets key-value pairs in collection and returns
    a list of all pairs
    """
    columns = {"_id": 0, "key": 1, "value": 1}
    results = collection.find({}, columns)
    return list(results)


def get_key(key) -> dict:
    """get_key function gets the matching key and value returns a dict of the
    key-value pair else it raises a KetNotFound error
    """
    columns = {"_id": 0, "key": 1, "value": 1}
    results = collection.find_one({"key": key}, columns)
    if results:
        return results
    raise KeyNotFound


def create_key(key, value) -> dict:
    """create_key function inserts a key-value pair to collection if the 'key'
    doesn't exist else it raises a KeyExists error
    """
    results = collection.find({"key": key})
    if not list(results):
        collection.insert_one({"key": key, "value": value})
        return {"key": key, "value": value}
    raise KeyExists


def update_key(key, value):
    """update_key function updates a key-value pair in collection if the 'key'
    exist else it raises a KeyNotFound error
    """
    results = collection.find({"key": key})
    if list(results):
        collection.update_one({"key": key}, {"$set": {"value": value}})
        return {
            "key": key,
            "value": value
        }
    raise KeyNotFound

