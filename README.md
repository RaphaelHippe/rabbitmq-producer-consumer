# Example for a Producer-Consumer-Service with RabbitMQ

## Usage

I run this example on my windows machine using a RabbitMQ running in Docker.

- create python venv `python -m venv venv`
- activcate the venv `./venv/Scripts/acticvate`
- install requirements `pip install -r requirements.txt`
- run main.py `python main.py`

## Ouput

When I run the example application I get the following output.

```
$ python main.py
INFO:root:Start listening to messages... on exchange: example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x00s.' to exchange: example with routing key: hello.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x00s.' to exchange: example with routing key: hello.example
INFO:root:Received message: {'count': 0} from exchange: example with routing key: hello.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x01s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x01s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 1} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x02s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x02s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 2} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x03s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x03s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 3} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x04s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x04s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 4} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x05s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x05s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 5} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x06s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x06s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 6} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x07s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x07s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 7} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x08s.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x08s.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 8} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\ts.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\ts.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 9} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\ns.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\ns.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 10} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0bs.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0bs.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 11} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0cs.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0cs.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 12} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\rs.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\rs.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 13} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0es.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0es.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 14} from exchange: example with routing key: routingkey.example
INFO:root:Publishing message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0fs.' to exchange: example with routing key: routingkey.example
INFO:root:Published message: b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05count\x94K\x0fs.' to exchange: example with routing key: routingkey.example
INFO:root:Received message: {'count': 15} from exchange: example with routing key: routingkey.example
```