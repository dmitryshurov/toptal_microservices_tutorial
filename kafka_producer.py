from confluent_kafka import KafkaError, KafkaException, Producer

from kafka_producer_message import ProducerMessage
from kafka_settings import KafkaSettings

class KafkaProducer:
    def __init__(self, settings: KafkaSettings):
        self._producer = Producer(settings.conf)

    def produce(self, message: ProducerMessage):
        try:
            self._producer.produce(message.topic, key=message.key, value=message.value)
            self._producer.flush()
        except KafkaException as exc:
            if exc.args[0].code() == KafkaError.MSG_SIZE_TOO_LARGE:
                pass  # Handle the error here
            else:
                raise exc
