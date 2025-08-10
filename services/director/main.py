import os
import sys
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from shared import pubsub_utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Director Service", description="Manages task orchestration and agent communication")

class MessagePayload(BaseModel):
    message: str
    attributes: dict = {}

@app.get("/")
def read_root():
    return {"message": "Director Service is running"}

@app.post("/publish-event")
async def publish_event(payload: MessagePayload):
    """
    Publishes a message to the 'salon-agent-events' Pub/Sub topic.
    """
    try:
        topic_name = "salon-agent-events"
        pubsub_utils.publish_message(payload.message, payload.attributes, topic_name=topic_name)
        logger.info(f"Published message to {topic_name}: {payload.message}")
        return {"status": "success", "message": "Event published successfully"}
    except Exception as e:
        logger.error(f"Error publishing event: {e}")
        return {"status": "error", "message": f"Failed to publish event: {e}"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
