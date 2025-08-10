
import os
from google.cloud import pubsub_v1

project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "salon-autonomous-ai-467811")
topic_name = "salon-events"
subscription_name = "salon-events-sub"

def publish_message(message_data: str, attributes: dict = None, topic_name: str = "salon-events"):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    data = message_data.encode("utf-8")

    if attributes is None:
        attributes = {}

    future = publisher.publish(topic_path, data, **attributes)
    print(f"Published message ID: {future.result()}")

def subscribe_messages(timeout: float = None):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message: pubsub_v1.subscriber.message.Message):
        print(f"Received message: {message.data.decode('utf-8')}")
        if message.attributes:
            print("Attributes:")
            for key, value in message.attributes.items():
                print(f"  {key}: {value}")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}")
    print() # Add a separate newline

    try:
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()

