from flask import Flask, render_template, request, jsonify

# Initialize app
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return jsonify({"message": "POST request received."})
    if request.method == "GET":
        return jsonify({"message": "Magician server is running at port: 5000"})


@app.route("/", methods=['PUT', 'DELETE'])
def index_two():
    if request.method == "PUT":
        return jsonify({"message": "PUT request received."})
    if request.method == "DELETE":
        return jsonify({"message": "DELETE request received."})


if(__name__ == '__main__'):
    app.run(debug=True)
