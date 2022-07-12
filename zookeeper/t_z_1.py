from kafka import KafkaConsumer
from collections import namedtuple


TopicPartition = namedtuple("TopicPartition", ["topic", "partition"])

kc = KafkaConsumer()
kc.next_v1()
kc.subscription()