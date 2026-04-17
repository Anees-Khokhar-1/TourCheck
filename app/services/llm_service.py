import requests
from app.config import settings

def call_llm(prompt):

    response = requests.post(
        "https://ai-gateway.vercel.sh/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {settings.MISTRAL_API_KEY}"
        },
        json={
            "model": "mistral/ministral-3b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0
        }
    )

    return response.json()["choices"][0]["message"]["content"]
