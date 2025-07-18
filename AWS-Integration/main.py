from botocore.exceptions import NoCredentialsError, ClientError
from fastapi import FastAPI, HTTPException
import boto3
import subprocess



app = FastAPI()

s3 = boto3.client('s3')

print("Boto3 is working", s3)


@app.get("/health")
def health_check():
    result = 'Awesome'
    return result

@app.get("/test_file")
def get_s3_objects(key: str):
    try:
        response = s3.get_object(Bucket="sainathchottu-test-bucket", Key=key)
        print("response: ",type(response))
        content = response['Body'].read().decode('utf-8')
        return {"file": key, "content": content}
    except NoCredentialsError:
        raise HTTPException(status_code=401, detail="AWS credentials not found.")
    except ClientError as e:
        raise HTTPException(status_code=404, detail=f"Failed to read file: {e}")
