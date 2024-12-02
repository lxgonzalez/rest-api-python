from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/bye', methods=['GET'])
def farewell():
    name = request.args.get('name', 'Friend')
    return jsonify({"message": f"Goodbye, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)