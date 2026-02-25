import os
import requests
from dotenv import load_dotenv
from ..mail_sender.email_generator import generate_email


load_dotenv()
URL = "https://api.brevo.com/v3/smtp/email"
headers = {
    "accept": "application/json",
    "api-key": os.getenv("BREVO_API_KEY"),
    "content-type": "application/json"
}

def send_email(receiver_email, receiver_name):
    payload = {
        "sender": {
            "name": "Code Blue CPR Services",
            "email": os.getenv("SENDER_EMAIL")
        },
        "to": [
            {
                "email": receiver_email,
                "name": receiver_name
            }
        ],
        "subject": "Action Required – Confirm Your AHA Alignment in Atlas",
        "htmlContent": generate_email(receiver_name)
    }

    try:
        response = requests.post(URL, json=payload, headers=headers)
        if response.status_code == 201:
            print(f"Successfully sent Email to {receiver_email}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Connection Error: {e}")
