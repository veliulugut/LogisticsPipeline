from confluent_kafka import Producer, KafkaException, KafkaError
import socket
import json
from Docker.data_generator.dataGenerator import generate_mock_data

conf = {
    'bootstrap.servers': '192.168.1.75:9092',
    'client.id': socket.gethostname()
}

# Producer nesnesi oluşturma
producer = Producer(conf)

# Verinin Kafka'ya gönderileceği topic
topic = "logistics_topic"

# Kafka'ya mesaj gönderme callback fonksiyonu
def acked(err, msg):
    if err is not None:
        print(f"Mesaj gönderilemedi: {str(err)}")
    else:
        print(f"Mesaj gönderildi: {str(msg)}")

# Veriyi almak ve Kafka'ya göndermek için fonksiyon
def produce_data():
    try:
        # Mock veriyi oluştur
        mock_data = str(generate_mock_data())

        # Kafka'ya veriyi gönder
        producer.produce(topic, key="key", value=mock_data, callback=acked)

        # Veriyi göndermek için flush işlemi
        producer.flush()

    except KafkaException as exception:
        print(exception)
        kafka_error = exception.args[ 0 ]
        if kafka_error.code() == KafkaError._UNKNOWN_PARTITION:
            print( "Kafka Topic/Partition Does Not Exist!!" )

if __name__ == "__main__":
    # Veriyi üret ve gönder
    produce_data()

