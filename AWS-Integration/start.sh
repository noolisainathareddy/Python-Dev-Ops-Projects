#!/bin/bash

export AWS_ACCESS_KEY_ID=AKIATM343HXBA7S2V5GL
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=us-east-1


uvicorn main:app --reload --host 0.0.0.0 --port 8000