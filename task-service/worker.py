import pika
from config import Config

def callback(ch, method, properties, body):
    print("Received %r" % body)

connection = pika.BlockingConnection(pika.URLParameters(Config.RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
