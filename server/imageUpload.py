import requests

def upload():
  url = "https://api.lightxeditor.com/external/api/v2/uploadImageUrl"

  headers = {
  "Content-Type": "application/json",
  "x-api-key": "8ff027f62a6b46cf83be38382d7fa97d_c21115d7d70e4863bcceedcab7d79154_andoraitools"
  }

  data = {
  "uploadType": "styleImageUrl",
  "size": 791436,
  "contentType": "image/jpeg"
  }

  response = requests.post(url, headers=headers, json=data)
  response = response.json()
  maskURL = response["body"]["styleImageUrl"]

  print(maskURL)
  file_path = r"/Users/abdullahsyed/projects/ai-professional-photo/server/test.jpeg"

  headers2 = {
  "Content-Type": "image/jpeg"
  }

  url = response["body"]["uploadImage"]
  with open(file_path, "rb") as file:
    response = requests.put(url, headers=headers2, data=file)
    print("hello")
  print(response.text)
  return response.text, maskURL
# print(response)