# from kafka import KafkaProducer
# # producer = KafkaProducer(bootstrap_servers='artobj.dev:9092')
# # producer = KafkaProducer(bootstrap_servers=['artobj.dev:9092'])
# producer = KafkaProducer(bootstrap_servers=['artwebs.dev:9092'],api_version=(0,10))
# while True:
#     producer.send('test1', b"test")
#     producer.send('test1', b"\xc2Hola, mundo!")
#     time.sleep(1)

from pykafka import KafkaClient
import logging
import sys
import json
from pykafka.partitioners import hashing_partitioner



if __name__ == '__main__':
    producer_logger = logging.getLogger('producer')
    logging.basicConfig(level = logging.WARN)
    # client = KafkaClient(hosts="artobj.dev:9092")
    client = KafkaClient(hosts="192.168.1.27:9092")
    topic = client.topics['my.test']
    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce('test message ' + str(i ** 2))
