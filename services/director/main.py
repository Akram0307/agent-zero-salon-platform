"""
Director Agent - Central orchestrator managing all other agents
"""

import os
import sys
# Add the project root to sys.path to ensure 'shared' module can be imported
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import logging
import asyncio

# Import shared utilities
from shared import pubsub_utils
from shared import firestore_utils
from google.cloud import firestore # Import firestore directly for SERVER_TIMESTAMP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Director Agent", description="Central orchestrator managing all other agents")

class TaskRequest(BaseModel):
    task_id: str
    task_type: str
    payload: dict

class TaskResponse(BaseModel):
    task_id: str
    status: str
    result: dict

# --- Pub/Sub Listener --- #
async def pubsub_listener():
    logger.info("Starting Pub/Sub listener...")
    # This is a simplified representation. In a production system,
    # you'd use a proper async Pub/Sub client or run the subscriber
    # in a separate process/thread managed by a process manager.
    # For now, we'll just log that it's listening.
    try:
        while True:
            # In a real scenario, you'd call pubsub_utils.subscribe_messages
            # and process messages here. This might require refactoring pubsub_utils
            # to be fully async or to use callbacks more effectively.
            # For this example, we'll simulate a continuous listener.
            await asyncio.sleep(5) # Simulate listening interval
            logger.info("Director Agent is actively listening for Pub/Sub messages...")

    except asyncio.CancelledError:
        logger.info("Pub/Sub listener cancelled.")
    except Exception as e:
        logger.error(f"Error in Pub/Sub listener: {e}")

@app.on_event("startup")
async def startup_event():
    logger.info("Director Agent starting up...")
    # Start the Pub/Sub listener in the background
    asyncio.create_task(pubsub_listener())

@app.get("/")
def read_root():
    return {"message": "Director Agent is running"}

@app.post("/task", response_model=TaskResponse)
async def process_task(task: TaskRequest):
    """
    Process a task by routing it to the appropriate agent via Pub/Sub.
    Also logs task processing to Firestore.
    """
    logger.info(f"Director: Received task {task.task_id} of type {task.task_type}")

    # Log task reception to Firestore
    firestore_log_data = {
        "task_id": task.task_id,
        "task_type": task.task_type,
        "payload": task.payload,
        "status": "received_by_director",
        "timestamp": firestore.SERVER_TIMESTAMP # Use server timestamp
    }
    log_doc_id = firestore_utils.add_document("director_task_logs", firestore_log_data)
    if log_doc_id:
        logger.info(f"Task {task.task_id} logged to Firestore with ID: {log_doc_id}")
    else:
        logger.error(f"Failed to log task {task.task_id} to Firestore.")

    # Publish task to Pub/Sub for the relevant agent to pick up
    # The 'task_type' can be used to route messages to specific agents/topics/subscriptions
    # For now, we'll publish to the general 'salon-events' topic.
    message_data = task.json()
    attributes = {"task_type": task.task_type, "task_id": task.task_id}
    pubsub_utils.publish_message(message_data, attributes)
    logger.info(f"Director: Published task {task.task_id} to Pub/Sub for type {task.task_type}")

    result = {
        "message": f"Task {task.task_id} of type {task.task_type} received and routed via Pub/Sub",
        "agent": "Director",
        "pubsub_message_published": True
    }

    return TaskResponse(task_id=task.task_id, status="routed", result=result)

@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
