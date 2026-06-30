from config import AI_PROVIDER
from services.ollama_client import analyze_logs as ollama_analyze
from services.openai_client import analyze_logs as openai_analyze

def analyze_logs(df):
    summary = f"""
Top actions:
{df['action'].value_counts().head()}

Top source IPs:
{df['source address'].value_counts().head()}

Top destination IPs:
{df['destination address'].value_counts().head()}

Denied count:
{(df['action'] == 'deny').sum()}
"""

    prompt = f"""
You are a cybersecurity analyst reviewing firewall traffic logs.

Here is a traffic summary:

{summary}

Write a concise analysis with these sections:
1. Overall traffic pattern
2. Potentially suspicious activity
3. Anything worth investigating further

Be specific and avoid vague filler.
"""

    if AI_PROVIDER == "openai":
        return openai_analyze(prompt)

    return ollama_analyze(prompt)