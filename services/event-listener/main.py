import os
import sys
import json
import base64
import logging
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from shared import pubsub_utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Event Listener Service", description="Listens for Pub/Sub events")

last_received_message = None

class PubSubMessage(BaseModel):
    message: dict
    subscription: str

@app.get("/")
def read_root():
    return {"message": "Event Listener Service is running"}

@app.post("/pubsub/push")
async def pubsub_push(request: Request):
    global last_received_message
    try:
        data = await request.json()
        message_data = base64.b64decode(data[\'message\'][\'data\']).decode(\'utf-8\')
        attributes = data[\'message\'].get(\'attributes\', {})
        message_id = data[\'message\'].get(\'messageId\')
        publish_time = data[\'message\'].get(\'publishTime\')

        logger.info(f"Received Pub/Sub message:")
        logger.info(f"  Message ID: {message_id}")
        logger.info(f"  Publish Time: {publish_time}")
        logger.info(f"  Attributes: {attributes}")
        logger.info(f"  Data: {message_data}")

        last_received_message = {
            "data": message_data,
            "attributes": attributes,
            "message_id": message_id,
            "publish_time": publish_time
        }

        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error processing Pub/Sub push message: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/last-received-message")
def get_last_received_message():
    if last_received_message:
        return {"status": "success", "message": last_received_message}
    else:
        return {"status": "no_message", "message": "No message received yet."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

