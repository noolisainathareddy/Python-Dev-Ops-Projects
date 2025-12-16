#!/bin/bash

export AWS_ACCESS_KEY_ID=<KeyID>
export AWS_SECRET_ACCESS_KEY=<AccessKey>
export AWS_DEFAULT_REGION=us-east-1


uvicorn main:app --reload --host 0.0.0.0 --port 8000