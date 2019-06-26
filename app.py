from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pdb

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

item = []

stores = [
    {
        'name': 'My great store',
        'items': [
            {
            'name':'My item',
            'price': 15.99
            }
        ]
    
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : [],
    }
    stores.append(new_store)
    return jsonify(stores)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store')
def get_stores():

    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):

    # pdb.set_trace()
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message':'store not found'})


    # new_store = {
    #     'name' : request_data['name'],
    #     'items' : [],
    # }
    # stores.append(new_store)

@app.route('/store/<string:name>/item')
def get_items_in_store(name):

    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message':'store not found'})

app.run(host="127.0.0.1",port=5001)
