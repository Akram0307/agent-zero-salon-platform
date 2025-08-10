import base64
import json
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

# Global variable to store the last received event for testing
last_received_booking_event = None

@app.get("/")
def read_root():
    return {"message": "Director service is running"}

@app.post("/pubsub/booking-events")
async def pubsub_booking_events(request: Request):
    global last_received_booking_event
    envelope = await request.json()

    if not envelope or 'message' not in envelope:
        raise HTTPException(status_code=400, detail="Invalid Pub/Sub message format")

    message = envelope['message']
    if 'data' not in message:
        raise HTTPException(status_code=400, detail="No data in Pub/Sub message")

    try:
        # Decode the base64-encoded data
        data_bytes = base64.b64decode(message['data'])
        event_data = json.loads(data_bytes.decode('utf-8'))

        # Check if it's a booking_created event
        if event_data.get('event_type') == 'booking_created':
            print(f"Received booking_created event: {event_data}")
            last_received_booking_event = event_data
        else:
            print(f"Received non-booking event: {event_data.get('event_type')}")

        return {"status": "success"}, 200
    except Exception as e:
        print(f"Error processing Pub/Sub message: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {e}")

@app.get("/last-booking-event")
def get_last_booking_event():
    if last_received_booking_event:
        return last_received_booking_event
    return {"message": "No booking event received yet"}
