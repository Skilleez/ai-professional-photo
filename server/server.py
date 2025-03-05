from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin
from image import image
from aws import upload_image, get_presigned
from pydantic import BaseModel
import json
from mongodb import store_url, images

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/", methods=['GET'])
@cross_origin()
def root():
  return jsonify({"message": "Hello this is working"})

@app.route("/data", methods=['POST'])
@cross_origin()
def data():
  x_user_id = request.headers.get("x_user_id")
  image_bytes = request.data
  key = upload_image(x_user_id, image_bytes)
  url = get_presigned(key)
  status = image(url)
  store_url(x_user_id, status, url)
  return jsonify({"message": "Image processed successfully"}), 200

@app.route("/images", methods=["GET"])
@cross_origin()
def get_images():
  x_user_id = request.headers.get("x_user_id")
  list = images(x_user_id)
  # json_list = json.dumps(list)
  print(jsonify(list))
  return jsonify(list)

