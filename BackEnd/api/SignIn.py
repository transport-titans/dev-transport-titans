from flask import Flask, request, jsonify

signin = Flask(__name__)


@signin.route("/signin", methods = ['POST'])
def SignIn():
    token = request.get_json()
    return jsonify({'message': 'Data received successfully', 'token': token}), 200

if __name__ == "__main__":
    signin.run(debug = True, port = '5001')