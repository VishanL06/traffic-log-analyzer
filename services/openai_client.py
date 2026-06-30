from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_logs(prompt):
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    return response.output_text