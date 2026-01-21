import pika
import json


RABBITMQ_HOST = 'localhost'


def get_connection():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    return connection


def publish(queue, message):
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(
    exchange='',
    routing_key=queue,
    body=json.dumps(message)
    )
    connection.close()

def consume(queue, callback):
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue)


    def wrapper(ch, method, properties, body):
        data = json.loads(body)
        callback(data)


    channel.basic_consume(queue=queue, on_message_callback=wrapper, auto_ack=True)
    print(f' [*] Aguardando mensagens em {queue}')
    channel.start_consuming()