import requests
from config import OLLAMA_URL, OLLAMA_MODEL

def analyze_logs(prompt):
    response = requests.post(
         OLLAMA_URL,
         json={
             "model": OLLAMA_MODEL,
             "prompt": prompt,
             "stream": False
         },
         timeout=120
      )

    response.raise_for_status()
    return response.json()["response"]