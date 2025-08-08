from flask import Flask, jsonify, request
from src.db.postgres_client import get_data_from_db
from src.model.neural_network import NeuralNetwork

app = Flask(__name__)
model = NeuralNetwork()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data)
    return jsonify({'prediction': prediction})

@app.route('/results', methods=['GET'])
def results():
    results_data = get_data_from_db()
    return jsonify(results_data)

if __name__ == '__main__':
    app.run(debug=True)