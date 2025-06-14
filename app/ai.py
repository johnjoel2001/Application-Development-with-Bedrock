import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set up Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "us-east-1")
)

def get_ai_suggestions(goal: str) -> list:
    """
    Generates task suggestions using Meta Llama 3.3 70B Instruct via Bedrock.
    """

    prompt = (
        "<|start_header_id|>user<|end_header_id|>\n"
        f"I want to accomplish the following goal: {goal}.\n"
        "Please suggest 3 specific and actionable tasks to help me.\n"
        "<|start_header_id|>assistant<|end_header_id|>"
    )

    payload = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.7,
        "top_p": 0.9
        # ❌ DO NOT include stop_sequences for Llama 3.3
    }

    try:
        response = bedrock.invoke_model(
            modelId="meta.llama3-3-70b-instruct-v1:0",
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json"
        )

        response_body = json.loads(response["body"].read())
        output = response_body.get("generation", "")

        return [
            line.strip("•-1234567890. ").strip()
            for line in output.strip().split("\n")
            if line.strip()
        ] or ["No suggestions were generated."]

    except Exception as e:
        print("Error calling Llama 3.3 via Bedrock:", e)
        return ["Failed to generate AI suggestions."]
