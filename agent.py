import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

def ask_health_question(question):
    payload = {
        # Changed to a highly reliable, ungated open model
        "model": "Qwen/Qwen2.5-7B-Instruct", 
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful personal health assistant. Give simple health advice. Do not replace professional medical advice."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Debug print to see exact error message text if it fails again
    if response.status_code != 200:
        print(f"Error Code: {response.status_code}")
        print(f"Server Response: {response.text}")
        
    response.raise_for_status()
    
    result = response.json()
    return result["choices"][0]["message"]["content"]