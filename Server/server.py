# Flask stuff
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import MySQLDatabase

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for any route


# db = MySQLDatabase('localhost', 'mydatabase', 'username', 'password', 'mytable')

@app.route('/get-rows', methods=['GET'])
def get_rows():
    address = request.args.get('address')

    # DUMMY DATA
    l: list = [
        ('john', 'brown', '892 e 700 n provo ut 84604', '800', 'covered', '949-709-9241'),
        ('mike', 'white', '1515 N 300 W st provo ut 84604', '800', 'uncovered', '949-632-6104'),
    ]

    # Placeholder response for testing
    return jsonify(l)
    
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
