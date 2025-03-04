import requests
import time
import json
from dotenv import load_dotenv
import os

load_dotenv()
phot_api_key = os.getenv('PHOT_API_KEY')

headers = {'x-api-key': phot_api_key}

def check_order_status(order_id):
    url = f"https://prodapi.phot.ai/external/api/v1/user_activity/order-status?order_id={order_id}"

    while True:
        response = requests.get(url, headers=headers, data={})
        
        try:
            data = response.json()
            order_status = data.get("order_status")
            print(f"🔍 Current Order Status: {order_status}")

            if order_status == "order_complete":
                print("✅ Order is complete!")
                return data
            elif order_status == "order_failed":
                return None

        except json.JSONDecodeError:
            print("❌ Error decoding JSON response.")

        time.sleep(5)


