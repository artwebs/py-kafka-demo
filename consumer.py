# from kafka import KafkaConsumer
# consumer = KafkaConsumer(bootstrap_servers=['artwebs.dev:9092'],api_version=(0,10))
# # consumer = KafkaConsumer(bootstrap_servers='artobj.dev:9092',
#                                 #  auto_offset_reset='earliest')
# consumer.subscribe(['test1'])
# for message in consumer:
#     print (message)

from pykafka import KafkaClient

if __name__ == '__main__':
    # client = KafkaClient(hosts="artobj.dev:9092")
    client = KafkaClient(hosts="192.168.1.27:9092")
    topic = client.topics['my.test']
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print message.offset, message.value
