import boto3
import uuid

s3 = boto3.client('s3')
bucket = "myawsbucketinsydneyforuni"

def upload_image(user_id, image):  
  file_name = f"{user_id}/{uuid.uuid4()}.jpg"
  s3.put_object(Bucket=bucket, Key=file_name, Body=image)
  return file_name

def get_image(user_id):
  url = []
  try:
    for item in s3.list_objects(Bucket=bucket)['Contents']:
      presigned_url = s3.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
      url.append(presigned_url)
  except Exception as e:
    pass
  print(url)
  return url


def get_presigned(key):
  try:
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": key},
        ExpiresIn=3600
    )
    return url
  
  except Exception as e:
    print("Error generating pre-signed URL:", e)
    return None
