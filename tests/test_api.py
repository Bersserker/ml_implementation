import requests
import pandas as pd


"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
def test_my_api(line):
    df = pd.read_csv('data/UCI_Credit_Card.csv').drop(columns=['ID','default.payment.next.month'])
    test_sample = df.iloc[line].tolist()
    test_sample = {'features':test_sample}
    resp = requests.post("http://0.0.0.0:5000/predict", json = test_sample, headers= header)

    print(resp.status_code)
    print(resp.json())


def test_rabbit(line):
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