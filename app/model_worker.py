import json
import pika
from rabbit_utils import send_to_y_pred
from model_handler import load_my_model, make_prediction
import os

predictions = os.getenv("QUEUE_NAME", "predictions")
y_pred = os.getenv("Y_QUEUE_NAME", "y_pred")
host = os.getenv("RABBIT_HOST", "localhost")
user = os.getenv("RABBIT_USER", "guest")
password = os.getenv("RABBIT_PASSWORD", "guest")

model = load_my_model()

def callback(ch, method, properties, body):
    message = json.loads(body)
    features = message["features"]
    print('мы внутри worker')
    prediction, proba = make_prediction(model, [features])

    print("callback отработал")
    print(f"{prediction=}")
    print(f"{proba=}")

    print(f'запись в {y_pred} очередь')

    result_message = {
            "features": features,
            "prediction": prediction,
            "probability": proba
        }

    send_to_y_pred(result_message)


    print('Запись завершена')

    ch.basic_ack(delivery_tag=method.delivery_tag)



credentials = pika.PlainCredentials(user, password)
params = pika.ConnectionParameters(
    host=host,
    credentials=credentials
)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=predictions, durable=True)
channel.queue_declare(queue=y_pred, durable=True)
channel.basic_consume(queue=predictions,on_message_callback=callback)
print("Обработчик заработал")
channel.start_consuming()