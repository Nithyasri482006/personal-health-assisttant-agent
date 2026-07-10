import os
import requests
import streamlit as st  # Added import
from dotenv import load_dotenv

load_dotenv()

# Check Streamlit Cloud secrets panel first, fall back to local .env
if "HF_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HF_TOKEN"]
else:
    HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

def ask_health_question(question):
    payload = {
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
    
    if response.status_code != 200:
        print(f"Error Code: {response.status_code}")
        print(f"Server Response: {response.text}")
        
    response.raise_for_status()
    
    result = response.json()
    return result["choices"][0]["message"]["content"]
