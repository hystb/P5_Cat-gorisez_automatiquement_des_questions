from flask import Flask, jsonify, request
# import mlflow

app = Flask(__name__)


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    # data = request.get_json()
    # model_uri = "models:/mon_modele/Production"
    # model = mlflow.pyfunc.load_model(model_uri)

    # prediction = model.predict([data['input']])
    prediction = ["python", "machine-learning", "data-science"]

    return jsonify({'tags': prediction})


@app.route('/api/v1/validate', methods=['POST'])
def validate():
    data = request.get_json()
    tags = data.get('tags')

    print(f'Tags validés: {tags}')

    return jsonify({'status': 'success', 'tags': tags})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
