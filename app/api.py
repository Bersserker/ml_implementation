from flask import Flask, request, jsonify
import pickle
from model_handler import laod_my_model, make_prediction

app = Flask(__name__)

# Загрузка модели
my_model = laod_my_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Получаем данные из POST-запроса
        prediction,proba = make_prediction(my_model, [data['features']])
        return jsonify({'prediction': prediction, 'probability': proba})
    except Exception as e:
        return jsonify({'error':str(e)}),400

@app.route('/health', methods=['GET'])
def health():
    return {"status":"ready_to_predict"} ,200

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000, debug=True)