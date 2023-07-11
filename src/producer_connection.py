import threading
import logging
import pickle
import os
from queue import Queue
import pika
import time

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.rabbitmq_user = os.getenv('RABBITMQ_USER')
        self.rabbitmq_pw = os.getenv('RABBITMQ_PW')
        self.rabbitmq_ip = os.getenv('RABBITMQ_IP')
        self.rabbitmq_port = os.getenv('RABBITMQ_PORT')

        self.exchange = os.getenv('EXCHANGE')

        self.connection = None
        self.channel = None
        self.message_queue = Queue()

    def createConnection(self):
        credentials = pika.PlainCredentials(self.rabbitmq_user, self.rabbitmq_pw)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbitmq_ip, self.rabbitmq_port, '/', credentials, heartbeat=5))
        self.channel = self.connection.channel()

    def publish(self, exchange, routing_key, body):
        logging.info('Publishing message: {} to exchange: {} with routing key: {}'.format(body, exchange, routing_key))
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body
        )
        logging.info('Published message: {} to exchange: {} with routing key: {}'.format(body, exchange, routing_key))


    def add_message(self, exchange, routing_key, message):
        self.message_queue.put({
            'exchange': exchange,
            'routing_key': routing_key,
            'body': pickle.dumps(message)
        })

    def run(self):
        self.createConnection()
        # declare your exchanges and bindings here
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='topic')
        
        # sleep 5 seconds
        time.sleep(5)
        
        self.add_message(self.exchange, 'hello.example', {'count': 0})

        while True:
            if not self.message_queue.empty():
                message = self.message_queue.get()
                self.publish(message['exchange'], message['routing_key'], message['body'])