import json
import pika
import os

predictions = os.getenv("QUEUE_NAME", "predictions")
y_pred = os.getenv("Y_QUEUE_NAME", "y_pred")
host = os.getenv("RABBIT_HOST", "localhost")
user = os.getenv("RABBIT_USER", "guest")
password = os.getenv("RABBIT_PASSWORD", "guest")

def send_to_queue(message: dict):
    credentials = pika.PlainCredentials(user, password)
    params = pika.ConnectionParameters(
        host=host,
        credentials=credentials
    )

    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue=predictions, durable=True)
    print(f'очередь {predictions} создана')

    channel.basic_publish(
        exchange="",
        routing_key=predictions,
        body=json.dumps(message)
    )
    connection.close()

def send_to_y_pred(message: dict):
    credentials = pika.PlainCredentials(user, password)
    params = pika.ConnectionParameters(
        host=host,
        credentials=credentials
    )

    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue=y_pred, durable=True)
    print(f'очередь {predictions} создана')

    channel.basic_publish(
        exchange="",
        routing_key=y_pred,
        body=json.dumps(message)
    )
    connection.close()