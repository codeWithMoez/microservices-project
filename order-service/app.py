from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/orders', methods=['GET'])
def create_order():
    order = {"order_id": 1, "user_id": 1, "product_id": 2}
    return jsonify(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
