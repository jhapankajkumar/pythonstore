from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': "My Books",
        'items': [
            {
                'name': "The Monk who sold his ferrari",
                'price': 20.30,
                'count': 30
            }
        ]
    }
]


@app.route('/')
def home():
    return "Welcome to our store"


# Post method to create store
@app.route('/store', methods=['POST'])
def create_store():
    print("Creating Store")
    name = request.json['name']
    print("Request Name: ", name)

    if get_store_from_name(name=name) is None:
        store = {
            'name': name,
            'items': []
        }
        stores.append(store)
        return jsonify(store)

    error = get_error('Duplicate Request', 404)
    return error


# Method to get store details
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)

    error = get_error("Resource not found", 404)
    return error


# Method to get list of all stores
@app.route("/store", methods=['GET'])
def get_all_store():
    return jsonify({'stores': stores})


# Method to add item to store
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item_to_store(name):
    item_name = request.json['name']
    print('ITEM NAME:', item_name)
    item_price = request.json['price']
    print('ITEM PRICE:', item_price)
    item_count = request.json['count']
    for store in stores:
        if name == store['name']:
            new_item = {'name': item_name,
                        'price': item_price,
                        'count': item_count
                        }
            store['items'].append(new_item)
            return jsonify({'item': new_item})

    error = get_error("Item Duplicate record found", 404)
    return error


# Method to get item in store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    item_name = request.json['name']
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['items']})
    else:
        return get_error("Item record found", 404)


# Method to update item
@app.route('/store/<string:name>/<string:item_name>', methods=['PUT'])
def update_item(name, item_name):
    item_price = request.json['price']
    item_count = request.json['count']
    for store in stores:
        if name == store['name']:
            for item in store['items']:
                if item['name'] == item_name:
                    item['price'] = item_price
                    item['count'] = item_count
                    return jsonify({'item': item})

    error = get_error("No record found", 404)
    return error


# Method to delete item from store
@app.route('/store/<string:name>/<string:item_name>', methods=['DELETE'])
def delete_item(name, item_name):
    for store in stores:
        if name == store['name']:
            for item in store['items']:
                if item['name'] == item_name:
                    store['items'].remove(item)
                    return jsonify({"message": "Record deleted successfully"})

    error = get_error("No record found", 404)
    return error


# Method to delete store from stores
@app.route('/store/<string:name>', methods=['DELETE'])
def delete_store(name):
    for store in stores:
        if name == store['name']:
            stores.remove(store)
            return jsonify({"message": "Record deleted successfully"})

    error = get_error("No record found", 404)
    return error


def get_store_from_name(name: str):
    for store in stores:
        if name == store['name']:
            return store


def get_error(message: str, error_code: int):
    error = {
        'error': {
            "description": message,
            "code": error_code
        }
    }
    return jsonify(error)


app.run()
