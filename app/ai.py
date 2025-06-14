import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "us-east-1")
)

def get_ai_suggestions(goal: str) -> list:
    prompt = f"""Human: I want to accomplish the goal: "{goal}".
Please suggest 3 specific and actionable tasks to help me achieve it.
Assistant:"""

    payload = {
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.7,
        "stop_sequences": ["\n\nHuman:"]
    }

    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-v2:1",
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json"
        )

        response_body = json.loads(response["body"].read())
        output = response_body.get("completion", "")

        return [
            line.strip("•-1234567890. ").strip()
            for line in output.strip().split("\n")
            if line.strip()
        ] or ["No suggestions were generated."]

    except Exception as e:
        print("Error calling Claude via Bedrock:", e)
        return ["Failed to generate AI suggestions."]
