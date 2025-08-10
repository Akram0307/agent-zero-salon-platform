import os
import sys
import logging
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..')) # Removed this line

from shared import pubsub_utils, firestore_utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Booking API Service", description="Handles salon booking operations")

class BookingRequest(BaseModel):
    service_name: str
    customer_id: str
    appointment_time: str # Use datetime for production

class BookingConfirmation(BaseModel):
    booking_id: str
    status: str
    message: str

@app.get("/")
def read_root():
    return {"message": "Booking API Service is running"}

@app.post("/create-booking", response_model=BookingConfirmation)
async def create_booking(request: BookingRequest):
    """
    Creates a new booking and publishes a booking_created event.
    """
    try:
        booking_id = str(uuid4())
        booking_data = request.dict()
        booking_data["booking_id"] = booking_id
        booking_data["status"] = "pending"

        # Save to Firestore
        firestore_utils.save_document("bookings", booking_id, booking_data)
        logger.info(f"Booking {booking_id} saved to Firestore.")

        # Publish booking_created event
        event_message = json.dumps({"event_type": "booking_created", "booking_id": booking_id, "customer_id": request.customer_id})
        event_attributes = {"booking_id": booking_id, "event_type": "booking_created"}
        pubsub_utils.publish_message(event_message, event_attributes, topic_name="salon-agent-events")
        logger.info(f"Booking created event published for booking {booking_id}.")

        return BookingConfirmation(booking_id=booking_id, status="pending", message="Booking request received and pending confirmation.")
    except Exception as e:
        logger.error(f"Error creating booking: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create booking: {e}")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
