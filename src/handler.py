from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/v1/predict', methods=['POST'])  
def predict():
    data = request.json
    return jsonify({"outputs": data["prompt"]})  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)