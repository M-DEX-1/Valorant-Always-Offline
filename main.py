import requests
import json
from requests.auth import HTTPBasicAuth

# Basic settings for the Valorant Local API
LOCAL_API_URL = "https://127.0.0.1:port/"
AUTH = HTTPBasicAuth("riot", "your_password")  # Check authentication details from the Riot client

# Function to change status to offline
def set_offline_status():
    try:
        # Change client status
        payload = {"status": "offline"}
        response = requests.put(
            f"{LOCAL_API_URL}chat/v1/me",
            auth=AUTH,
            json=payload,
            verify=False  # Ignore SSL verification
        )
        
        if response.status_code == 200:
            print("Successfully set to offline mode!")
        else:
            print("Failed to set offline status:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to check current status
def get_current_status():
    try:
        response = requests.get(
            f"{LOCAL_API_URL}chat/v1/me",
            auth=AUTH,
            verify=False
        )
        if response.status_code == 200:
            print("Current status:", json.loads(response.text))
        else:
            print("Failed to get status:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example execution
get_current_status()
set_offline_status()
