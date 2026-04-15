from flask import Flask, request, jsonify
from model_handler import load_my_model, make_prediction
from rabbit_utils import send_to_queue

app = Flask(__name__)

my_model = load_my_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prediction, proba = make_prediction(my_model, [data['features']])
        return jsonify({'prediction': prediction, 'probability': proba})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/predict_rabbit", methods=["POST"])
def predict_with_queue():
    try:
        data = request.get_json()
        send_to_queue({
            "features": data["features"]
        })
        return jsonify({'status': "сообщение отправлено в очередь"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/health', methods=['GET'])
def health():
    return {"status": "ready_to_predict"}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)