import json
import pika

predictions = 'predictions'
host = 'localhost'
def send_to_queue(message:dict):
    #подключение к брокеру
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    #создание обмена с именем logs 
    channel.queue_declare(queue=predictions)
    print(f'очередт {predictions} создана')
    channel.basic_publish(exchange="",routing_key=predictions,body=json.dumps(message))
    connection.close()