import json
import pika
from model_handler import laod_my_model, make_prediction
from rabbit_utils import predictions, host

model = laod_my_model()

def callback(ch, method, properties, body):
    message = json.loads(body)
    features = message['features']
    prediction, proba = make_prediction(model, [features])
    print('callback отработал')
    print(f'{prediction=}')
    print(f'{proba=}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))

channel = connection.channel()
channel.queue_declare(queue=predictions)

channel.basic_consume(queue=predictions, on_message_callback=callback)

print('Обработчик заработал')
channel.start_consuming()