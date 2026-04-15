import joblib
import pandas as pd

print('Загрузка модели')

model = None

def load_my_model():
    global model
    if model is None:
        model = joblib.load('models/model_v1.pkl')
    return model

def make_prediction(model,data):
    columns = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2',
       'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
    
    x = pd.DataFrame(data, columns=columns)
    prediction = int(model.predict(x)[0])
    proba = float(model.predict_proba(x)[:,1][0])
    #print(f'{prediction=}')
    #print(f'{proba=}')
    return prediction , proba
