
import os
from google.cloud import firestore

service_account_key_path = "/a0/tmp/uploads/salon-autonomous-ai-467811-fbe5da7865de.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key_path
os.environ["GOOGLE_CLOUD_PROJECT"] = os.getenv("GOOGLE_CLOUD_PROJECT", "salon-autonomous-ai-467811")

try:
    db = firestore.Client()
except Exception as e:
    print(f"Error initializing Firestore client: {e}")
    print("Please ensure Application Default Credentials are set up correctly.")
    print("Refer to https://cloud.google.com/docs/authentication/external/set-up-adc for more information.")
    raise # Re-raise the exception to indicate failure

def add_document(collection_name: str, data: dict, document_id: str = None):
    try:
        if document_id:
            doc_ref = db.collection(collection_name).document(document_id)
            doc_ref.set(data)
            return document_id
        else:
            update_time, doc_ref = db.collection(collection_name).add(data)
            return doc_ref.id
    except Exception as e:
        print(f"Error adding document: {e}")
        return None

def get_document(collection_name: str, document_id: str):
    try:
        doc_ref = db.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    except Exception as e:
        print(f"Error getting document: {e}")
        return None

def update_document(collection_name: str, document_id: str, data: dict):
    try:
        doc_ref = db.collection(collection_name).document(document_id)
        doc_ref.update(data)
        return True
    except Exception as e:
        print(f"Error updating document: {e}")
        return False

def delete_document(collection_name: str, document_id: str):
    try:
        db.collection(collection_name).document(document_id).delete()
        return True
    except Exception as e:
        print(f"Error deleting document: {e}")
        return False

def query_collection(collection_name: str, field: str, op: str, value: any):
    try:
        docs = db.collection(collection_name).where(field, op, value).stream()
        results = []
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id
            results.append(doc_data)
        return results
    except Exception as e:
        print(f"Error querying collection: {e}")
        return []
