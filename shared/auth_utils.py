
import os
import firebase_admin
from firebase_admin import credentials, auth

service_account_key_path = "/a0/tmp/uploads/salon-autonomous-ai-467811-fbe5da7865de.json"

try:
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    print("Please ensure the service account key path is correct and the file is valid.")
    raise

def create_user(email: str, password: str):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def get_user_by_email(email: str):
    try:
        user = auth.get_user_by_email(email)
        return user
    except Exception as e:
        print(f"Error fetching user by email: {e}")
        return None

def verify_id_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Error verifying ID token: {e}")
        return None
