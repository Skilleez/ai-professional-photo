from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin
from image import image
from aws import upload_image, get_presigned
from pydantic import BaseModel
import json
from mongodb import store_url, images
import traceback

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/", methods=['GET'])
@cross_origin()
def root():
  return jsonify({"message": "Hello this is working"})

@app.route("/data", methods=['POST'])
@cross_origin()
def data():
  x_user_id = request.headers.get("X-User-Id")
  if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
  image_bytes = request.files["file"].read()
  try:
    key = upload_image(x_user_id, image_bytes)
    url = get_presigned(key)
    status = image(url)
    res = store_url(x_user_id, status, url)
    return jsonify({"message": "Image processed successfully"}), 200
  except Exception as e:
    print("Error occurred:", e)
    traceback.print_exc()  # Print the full error stack trace
    return jsonify({"error": str(e)}), 400

@app.route("/images", methods=["GET"])
@cross_origin()
def get_images():
  x_user_id = request.headers.get("x_user_id")
  list = images(x_user_id)
  # json_list = json.dumps(list)
  print(jsonify(list))
  return jsonify(list)

