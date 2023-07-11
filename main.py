import logging
import os
import sys
import socketio
from dotenv import load_dotenv

from src.consumer_connection import Consumer
from src.producer_connection import Producer

def main():
    load_dotenv()

    RABBITMQ_USER = os.getenv('RABBITMQ_USER')
    RABBITMQ_PW = os.getenv('RABBITMQ_PW')
    RABBITMQ_IP = os.getenv('RABBITMQ_IP')
    RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')

    mgr = socketio.KombuManager('amqp://{}:{}@{}:{}//'.format(RABBITMQ_USER, RABBITMQ_PW, RABBITMQ_IP, RABBITMQ_PORT), write_only=True)

    producer = Producer()
    consumer = Consumer(producer, mgr)

    producer.start()
    consumer.start()

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("pika").propagate = False
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
    
    
    
