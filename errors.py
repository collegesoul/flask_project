class KeyNotFound(Exception):
    """Raised when a key in a dictionary, json or no-sql database does not exist"""
    def __init__(self):
        print("This key does not exist")


class KeyExists(Exception):
    """Raised when a new key uses an identifier of an already existing key in a dictionary, json or no-sql database"""
    def __init__(self):
        print("This key already exist")


# Custom error messages for errors
messages = {
    "empty-body": {"message": "key and value parameters should not be empty"},
    "invalid-format": {"message": "invalid use of body parameters: use 'key' and 'value' for parameters"},
    "key-not-found": {"message": "no such key exists"},
    "key-exists": {"message": "cannot create key as key already exists"},
    "no-content": {"message": "no Content Found"}
}
