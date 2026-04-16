import requests
import pandas as pd


"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
def test_my_api(line):
    """
    Предсказание модели.
    Формат запроса:
    {
        features': [90000.0, 2.0, 2.0, 2.0, 34.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 29239.0, 14027.0, 13559.0, 14331.0, 14948.0, 15549.0, 1518.0, 1500.0, 1000.0, 1000.0, 1000.0, 5000.0]
    }

    Формат ответа (успех):
    {
        "prediction": 1,           # класс/значение предсказания (int/float)
        "probability": 0.92       # вероятность (float, 0–1)
    }
    """
    df = pd.read_csv('data/UCI_Credit_Card.csv').drop(columns=['ID','default.payment.next.month'])
    test_sample = df.iloc[line].tolist()
    test_sample = {'features':test_sample}
    resp = requests.post("http://0.0.0.0:5000/predict", json = test_sample, headers= header)
    print(test_sample)
    print(resp.status_code)
    print(resp.json())


def test_rabbit(line):
    """
    Предсказание модели.
    Формат запроса:
    {
        features': [90000.0, 2.0, 2.0, 2.0, 34.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 29239.0, 14027.0, 13559.0, 14331.0, 14948.0, 15549.0, 1518.0, 1500.0, 1000.0, 1000.0, 1000.0, 5000.0]
    }

    Формат ответа (успех):
    {
        "prediction": 1,           # класс/значение предсказания (int/float)
        "probability": 0.92       # вероятность (float, 0–1)
    }
    """
    df = pd.read_csv('data/UCI_Credit_Card.csv').drop(columns=['ID','default.payment.next.month'])
    test_sample = df.iloc[line].tolist()
    test_sample = {'features':test_sample}
    resp = requests.post("http://0.0.0.0:5000/predict_rabbit", json = test_sample, headers= header)

    print(resp.status_code)
    print(resp.json())

test_my_api(0)
test_my_api(2)

test_rabbit(0)
test_rabbit(2)