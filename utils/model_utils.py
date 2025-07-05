import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/bigscience/T0pp"
API_KEY = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {API_KEY}"}

# def call_llm(prompt):
#     response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
#     if response.status_code == 200:
#         return response.json()[0]["generated_text"]
#     else:
#         return f"⚠️ LLM Error: {response.status_code} - {response.text}"
prompt = "Explain the benefits of using drones in agriculture."

response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
print(response.status_code)
print(response.text)