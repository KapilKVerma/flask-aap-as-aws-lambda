from flask import Flask, render_template, request, jsonify

# Initialize app
app = Flask(__name__)

items = [{
    "id": 1,
    "name": "product 1 name",
    "description": "This is the first product description"
}]


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        item_data = request.get_json()
        print(item_data)
        items.append(item_data)
        return jsonify({"items": items})
    if request.method == "GET":
        return jsonify({"message": "Magician server is running at port: 5000"})


@app.route("/<int:id>", methods=['PUT', 'DELETE'])
def index_two(id):
    if request.method == "PUT":
        return jsonify({"message": "PUT request received."})
    if request.method == "DELETE":
        items.remove({'id': id})
        print(id)
        return jsonify({"message": "DELETE request received."})


if(__name__ == '__main__'):
    app.run(debug=True)
