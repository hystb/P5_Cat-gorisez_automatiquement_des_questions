from flask import Flask, jsonify, request
from model import model_api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    data = request.get_json()
    title = data['question']
    response = model_api.predict(title)
    return jsonify(response)


@app.route('/api/v1/validate', methods=['POST'])
def validate():
    data = request.get_json()
    tags = data.get('tags')

    print(f'Tags validés: {tags}')

    return jsonify({'status': 'success', 'tags': tags})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
