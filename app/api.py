from flask import Flask, request, jsonify
import pickle
from app.model_handler import laod_my_model, make_prediction

app = Flask(__name__)

# Загрузка модели
my_model = laod_my_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Получаем данные из POST-запроса
    prediction = make_prediction(my_model, [data['features']])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/health', methods=['GET'])
def health():
    return {"status":"ready_to_predict"} ,200

if __name__ == "__main__":
    app.run(debug=True)