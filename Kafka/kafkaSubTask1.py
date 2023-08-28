from kafka import KafkaProducer

# Kafka broker settings
bootstrap_servers = 'localhost:9092'

# Create a Kafka producer instance
# producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))


# Topic to send messages to
topic = 'firstTopic'

# Messages to send
messages = [
    'Hello, Kafka!',
    'This is message from Intelli J Idea.',
    "I'm not an impostor."
]

# Produce messages to the topic
for message in messages:
    producer.send(topic, value=message.encode('utf-8'))

# Wait for any outstanding messages to be delivered
producer.flush()

print(f"Messages sent to '{topic}' topic.")

# Close the producer to release resources
producer.close()
