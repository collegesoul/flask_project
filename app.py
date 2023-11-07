from flask import Flask, request, jsonify
import db
from errors import *

app = Flask(__name__)


@app.get('/api/v1/keys')
def get_keys():
    key_value_pairs = db.get_keys()
    if not key_value_pairs:
        return jsonify(messages["no-content"])
    return jsonify(key_value_pairs), 200


@app.get('/api/v1/key/<key>')
def get_key(key):
    try:
        key_value_pair = db.get_key(key)
    except KeyNotFound:
        return jsonify(messages["key-not-found"]), 404
    else:
        return jsonify(key_value_pair), 200


@app.post('/api/v1/key')
def create_key():
    data = request.get_json()
    try:
        key = data['key']
        value = data['value']
    except KeyError:
        return jsonify(messages["invalid-format"]), 404
    else:
        if key and value:
            try:
                new_key_value_pair = db.create_key(key, value)
            except KeyExists:
                return jsonify(messages["key-exists"]), 400
            else:
                return jsonify(new_key_value_pair), 201
        return jsonify(messages["empty-body"]), 400


@app.put('/api/v1/key')
def update_key():
    data = request.get_json()
    try:
        key = data['key']
        value = data['value']
    except KeyError:
        return jsonify(messages["invalid-format"]), 404
    else:
        if key and value:
            try:
                key_value_pair = db.update_key(key, value)
            except KeyNotFound:
                return jsonify(messages["key-not-found"]), 404
            else:
                return jsonify(key_value_pair), 200
        return jsonify(messages["empty-body"]), 400


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
