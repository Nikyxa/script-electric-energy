from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql123",
    database="electricity_market_data",
)


@app.route('/data', methods=['GET'])
def get_data():
    date = request.args.get('date')

    if not date:
        return jsonify({'error': 'No date provided'})

    cursor = db.cursor()

    query = "SELECT * FROM electricity_market_data WHERE date = %s"
    cursor.execute(query, (date,))
    result = cursor.fetchall()

    cursor.close()
    db.close()

    data = []
    for row in result:
        record = {
            'date': row[0],
            'hour': row[1],
            'price': row[2],
            'volume': row[3],
        }
        data.append(record)

    return jsonify(data)


if __name__ == '__main__':
    app.run()

