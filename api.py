# api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulating an in-memory database (list of items)
items = [
    {"id": 1, "name": "Item A", "status": "pending"},
    {"id": 2, "name": "Item B", "status": "complete"}
]
next_id = 3

@app.route('/items', methods=['GET'])
def get_items():
    """Returns the list of all items."""
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def add_item():
    """Adds a new item to the list."""
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    new_item = {
        "id": next_id,
        "name": data['name'],
        "status": "new"
    }
    items.append(new_item)
    next_id += 1
    
    # Integration point: Returns the newly created item, confirming database interaction.
    return jsonify(new_item), 201

if __name__ == '__main__':
    # Running on a specific port for testing
    app.run(debug=True, port=5000)