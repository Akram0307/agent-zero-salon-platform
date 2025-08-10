import json
from fastapi import FastAPI
from google.cloud import pubsub_v1

app = FastAPI()

# Configure Pub/Sub client
project_id = "salon-autonomous-ai-467811"
topic_id = "salon-agent-events"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

@app.post("/create-booking")
async def create_booking():
    event_data = {
        "event_type": "booking_created",
        "booking_id": "12345",
        "customer_id": "67890",
        "service": "haircut"
    }
    data = json.dumps(event_data).encode("utf-8")
    
    try:
        future = publisher.publish(topic_path, data)
        message_id = future.result()
        print(f"Published message {message_id} to {topic_path}")
        return {"message": "Booking created and event published", "message_id": message_id}
    except Exception as e:
        print(f"Error publishing message: {e}")
        return {"message": "Error publishing event"}, 500

@app.get("/")
def read_root():
    return {"message": "Booking API is running"}
