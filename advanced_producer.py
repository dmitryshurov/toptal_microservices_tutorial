from dotenv import load_dotenv

from kafka_producer import KafkaProducer
from kafka_producer_message import ProducerMessage
from kafka_settings import KafkaSettings

def main():
    settings = KafkaSettings()
    producer = KafkaProducer(settings)
    message = ProducerMessage(
        topic='MyFirstKafkaTopic',
        value={"value": "MyFirstKafkaValue"},
        key=None,
    )
    producer.produce(message)

if __name__ == '__main__':
    load_dotenv()
    main()
