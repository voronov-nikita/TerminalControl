from flask import Flask, jsonify,request


app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'pin': 10,
        'temperature': 30,
        'humidity': 100
    }
    return jsonify(data)


@app.route('/post', methods=['POST'])
def post_request():
    data = request.json
    data['key1'] = 100
    data['key2'] = 200
    return jsonify(data)


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)