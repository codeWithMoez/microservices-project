from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/products', methods=['GET'])
def get_products():
    products = [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Smartphone"}]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
