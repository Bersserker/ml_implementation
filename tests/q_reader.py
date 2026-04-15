import json
import pika
import os

y_pred = "prediction_results"
user = "appuser"
password = "apppass"
host = "localhost"


def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Получен результат:", message, flush=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials(user, password)
params = pika.ConnectionParameters(
    host=host,
    credentials=credentials
)

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=y_pred, durable=True)

channel.basic_consume(
    queue=y_pred,
    on_message_callback=callback
)

print("Чтение очереди результатов запущено", flush=True)
channel.start_consuming()