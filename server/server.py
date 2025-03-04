from fastapi import FastAPI, Header, Request
from image import image
from aws import upload_image, get_presigned
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from mongodb import store_url, images

app = FastAPI()
origins = [
    "https://ai-professional-photo.vercel.app",
    "https://ai-professional-photo.vercel.app/data",
    "https://ai-professional-photo.vercel.app/images",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# sample = {'order_status_code': 200, 'order_status': 'order_complete', 
#           'output_urls': ['https://photai-s3-bucket.apyhi.com/background_generator/output_image/2025-03-03/hmxf4ey_2025-03-03T07:17:55.906Z_output_0.webp', 'https://photai-s3-bucket.apyhi.com/background_generator/output_image/2025-03-03/hmxf4ey_2025-03-03T07:17:55.906Z_output_1.webp', 'https://photai-s3-bucket.apyhi.com/background_generator/output_image/2025-03-03/hmxf4ey_2025-03-03T07:17:55.906Z_output_2.webp', 'https://photai-s3-bucket.apyhi.com/background_generator/output_image/2025-03-03/hmxf4ey_2025-03-03T07:17:55.906Z_output_3.webp']}


@app.get("/")
async def root():
  return {"message": "Hello this is working"}

@app.post("/data")
async def data(request: Request, x_user_id: str = Header(None)):
  image_bytes = await request.body()
  key = upload_image(x_user_id, image_bytes)
  url = get_presigned(key)
  status = image(url)
  store_url(x_user_id, status, url)
  return

@app.get("/images")
async def get_images(x_user_id: str = Header(None)):
  list = images(x_user_id)
  json_list = json.dumps(list)
  print(json_list)
  return json_list