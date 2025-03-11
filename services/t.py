import requests

API_KEY = "AIzaSyB05YYb4DG9Y_FWW5pSK8yQUSK2fyfPZP4"
url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

response = requests.get(url)
print(response.json())  # This will list the available models



from typing import List
import google.generativeai as genai  
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_bios(about_me: str) -> List[str]:
    prompt = f"Generate 4 professional bio descriptions based on: {about_me}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    bios = response.text.split("\n")[:4]  
    return bios
