import requests
from config import AI_API_KEY

def get_ai_response(query):
    url = "https://api.gemini-ai.com/generate"
    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    payload = {"prompt": query}
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "I couldn't generate a response.")
    return "Error communicating with AI API."
