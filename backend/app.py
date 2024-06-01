from flask import Flask, request, jsonify
from flask_cors import CORS
import robertacolab

app = Flask(__name__)
cors = CORS(app)
# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"

@app.route("/")
def root():
    print("received request at /")
    return "Unsupported Request"

@app.route("/receiver", methods=["POST"])
def postME():
    data = request.get_json()
    # print(data)
    # print(data)
    return jsonify(robertacolab.result(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
