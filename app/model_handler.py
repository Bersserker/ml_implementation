import joblib

print('Загрузка модели')

model = None

def laod_my_model():
    global model
    if model is None:
        model = joblib.load('models/model_v1.pkl')
    return model

def make_prediction(model,data):
    return model.predict(data)