from flask import Flask, request, jsonify
import uuid
from utils import count_points

app = Flask(__name__)

receiptToPoint = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        data = request.json
        receipt_id = str(uuid.uuid4())
        point = count_points(data)
        receiptToPoint[receipt_id] = point
        return jsonify({"id": receipt_id}), 200
    except Exception as e:
        print(f"Error processing receipt: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/receipts/<string:id>/points', methods=['GET'])
def get_receipt_points(id):
    try:
        if id in receiptToPoint:
            return jsonify({"points": receiptToPoint[id]}), 200
        else:
            return jsonify({"error": "No receipt found for that id"}), 404
    except Exception as e:
        print(f"Error getting receipt [pomts]: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
