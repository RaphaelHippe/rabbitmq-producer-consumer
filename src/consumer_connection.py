import threading
import logging
import pika
import os
import functools
import time
import pickle

class Consumer(threading.Thread):
    def __init__(self, producer, mgr):
        threading.Thread.__init__(self)

        self.rabbitmq_user = os.getenv('RABBITMQ_USER')
        self.rabbitmq_pw = os.getenv('RABBITMQ_PW')
        self.rabbitmq_ip = os.getenv('RABBITMQ_IP')
        self.rabbitmq_port = os.getenv('RABBITMQ_PORT')

        self.exchange = os.getenv('EXCHANGE')

        self.producer = producer
        self.mgr = mgr

        self.connection = None
        self.channel = None

    def createConnection(self):
        credentials = pika.PlainCredentials(self.rabbitmq_user, self.rabbitmq_pw)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbitmq_ip, self.rabbitmq_port, '/', credentials, heartbeat=5))
        self.channel = self.connection.channel()

    def ack_message(self, channel, delivery_tag):
        """Note that `channel` must be the same pika channel instance via which
        the message being ACKed was retrieved (AMQP protocol constraint).
        """
        if channel.is_open:
            channel.basic_ack(delivery_tag)
        else:
            # Channel is already closed, so we can't ACK this message;
            # log and/or do something that makes sense for your app in this case.
            pass

    def do_work(self, connection, channel, delivery_tag, routing_key, body):
        #################### START OF LOGIC ####################
        message = pickle.loads(body)
        logging.info('Received message: {} from exchange: {} with routing key: {}'.format(message, self.exchange, routing_key))


        # sleep for 2 seconds to simulate heavy work
        time.sleep(2)

        if message['count'] < 15:
            message['count'] += 1
            # during message handling send more messages to rabbitmq
            self.producer.add_message(self.exchange, 'routingkey.example', message)

        #################### END OF LOGIC ####################
        cb = functools.partial(self.ack_message, channel, delivery_tag)
        connection.add_callback_threadsafe(cb)

    def on_message(self, channel, method, header_frame, body, args):
        (connection, threads) = args
        delivery_tag = method.delivery_tag
        routing_key = method.routing_key
        t = threading.Thread(target=self.do_work, args=(connection, channel, delivery_tag, routing_key, body))
        t.start()
        threads.append(t)

    def run(self):
        self.createConnection()

        # declare your exchanges and bindings here
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='topic')
        
        # example queue declaration
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key='*.example')
        
        self.channel.basic_qos(prefetch_count=1)

        threads = []
        on_message_callback = functools.partial(self.on_message, args=(self.connection, threads))
        self.channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback, auto_ack=False)

        logging.info('Start listening to messages... on exchange: {}'.format(self.exchange))
        self.channel.start_consuming()

        # Wait for all to complete
        for thread in threads:
            thread.join()
