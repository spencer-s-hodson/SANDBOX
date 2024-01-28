# Flask stuff
from flask import Flask, request, jsonify
from flask_cors import CORS
from Database.database import MySQLDatabase

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for any route


# db = MySQLDatabase('localhost', 'mydatabase', 'username', 'password', 'mytable')

@app.route('/get-rows', methods=['GET'])
def get_rows():
    address = request.args.get('address')

    # Placeholder response for testing
    return jsonify({"message": "Received address: " + str(address)})
    
    # rows = db.query_data()
    # return jsonify(rows)

@app.route('/insert-row', methods=['GET', 'POST'])
def insert_row():
    data = request.get_json()
    print(data)
    # db.insert_data(data)
    return jsonify({"message": "Row inserted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
