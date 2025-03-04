import requests
from imageUpload import upload
from order import check_order_status
from dotenv import load_dotenv
import os


def image(input_url):
	load_dotenv()
	url = 'https://prodapi.phot.ai/external/api/v3/user_activity/background-generator'
  
	phot_api_key = os.getenv('PHOT_API_KEY')
  
	headers = {
      'x-api-key': phot_api_key,
      'Content-Type': 'application/json'
  }
	data = {
      'source_url': input_url
  }
  
	data['prompt'] = "professional office background"
  
	response = requests.post(url, headers=headers, json=data)
  

	print(response.status_code)
	response = response.json()
	order_id = response["order_id"]
	print(order_id)
  
  
	d = check_order_status(order_id)
	print(d)
	return d
  