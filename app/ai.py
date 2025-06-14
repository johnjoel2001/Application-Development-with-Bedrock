import boto3
import json
import os

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION")
)

def get_ai_suggestions(goal: str) -> list:
    """Call Amazon Bedrock with a goal, return a list of tasks."""
    prompt = f"\n\nHuman: I want to accomplish: {goal}. Give me 3 specific tasks.\n\nAssistant:"
    payload = {
        "prompt": prompt,
        "max_tokens_to_sample": 200,
        "temperature": 0.7,
        "stop_sequences": ["\n\nHuman:"]
    }

    response = bedrock.invoke_model(
        body=json.dumps(payload),
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())
    text = response_body.get("completion", "")
    return [line.strip("•- ").strip() for line in text.strip().split("\n") if line.strip()]
