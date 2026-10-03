# Amazon Bedrock integration placeholder.
# Keep numeric scoring deterministic in the backend.
# Bedrock should be used for personalized explanations and roadmap generation.

import os
import boto3

def get_bedrock_client():
    region=os.getenv("AWS_REGION","ap-south-1")
    return boto3.client("bedrock-runtime",region_name=region)
