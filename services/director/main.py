import os
import sys
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from shared import pubsub_utils
from shared import firestore_utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Director Service", description="Manages task orchestration and agent communication")

class MessagePayload(BaseModel):
    message: str
    attributes: dict = {}

class FirestoreTestData(BaseModel):
    collection_name: str
    document_id: str
    data: dict

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

@app.post("/firestore-test")
async def firestore_test(payload: FirestoreTestData):
    """
    Saves and retrieves a document from Firestore for testing.
    """
    try:
        # Save document
        firestore_utils.save_document(
            payload.collection_name,
            payload.document_id,
            payload.data
        )
        logger.info(f"Saved document {payload.document_id} to collection {payload.collection_name}")

        # Retrieve document
        retrieved_data = firestore_utils.get_document(
            payload.collection_name,
            payload.document_id
        )
        logger.info(f"Retrieved document {payload.document_id}: {retrieved_data}")

        return {"status": "success", "saved_data": payload.data, "retrieved_data": retrieved_data}
    except Exception as e:
        logger.error(f"Error during Firestore test: {e}")
        return {"status": "error", "message": f"Firestore test failed: {e}"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
