
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pydantic import BaseModel
import certifi
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, tlsCAFile=certifi.where())
database = client.image
collection = database.images

class ImageData(BaseModel):
    user_id: str
    original_image: str
    generated_images: list[str]

def store_url(user_id, status: ImageData, url):
    try:
        record = {
            "user_id": user_id,
            "original_image": url,
            "generated_images": status["output_urls"]
        }
        result = collection.insert_one(record)
        print(result.acknowledged)

    except Exception as e:
        print(e)

    finally:
        client.close()


def images(user_id):
    client = MongoClient(uri, tlsCAFile=certifi.where())
    database = client.image
    collection = database.images
    list = []
    records = collection.find({ "user_id": user_id})
    for doc in records:
        list += doc['generated_images']
    return list