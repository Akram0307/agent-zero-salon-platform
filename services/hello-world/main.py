from fastapi import FastAPI
from shared.pubsub_utils import publish_message
from shared.firestore_utils import get_document

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World! This is the minimal salon-platform service."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-shared")
def test_shared_utilities():
    try:
        # Test Pub/Sub utility
        publish_message("Test message from hello-world service")

        # Test Firestore utility (try to get a non-existent document)
        doc = get_document("test-collection", "test-document-id")

        return {
            "pubsub": "Message published successfully",
            "firestore": f"Document retrieval result: {doc}",
            "status": "Shared utilities are working correctly"
        }
    except Exception as e:
        return {
            "error": str(e),
            "status": "Failed to test shared utilities"
        }
