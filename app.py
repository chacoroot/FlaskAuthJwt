from flask import Flask, jsonify

app = Flask(__name__)

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
    pass

@app.route('/store/<string:name>')
def get_store(name):

    return name

@app.route('/store')
def get_stores():

    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):

    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):

    return name

app.run(host="127.0.0.1",port=5001)
