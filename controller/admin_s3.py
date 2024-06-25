import boto3
from credentials.keys import ACCES_KEY, SECRET_KEY

def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCES_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Conectado a S3")
    except Exception as err:
        print("Error", err)
        
def save_file(photo):
    try:
        photo_path = "/tmp/photo.JPEG"
        photo.save(photo_path)
        print("Foto guardada")
    except Exception as err:
        print("Error", err)