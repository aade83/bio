from typing import List
import google.generativeai as genai  # Using Gemini API
import os

# Configure Gemini API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_bios(about_me: str) -> List[str]:
    prompt = f"Generate 4 professional bio descriptions based on: {about_me}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    bios = response.text.split("\n")[:4]  # Extracting first 4 bios
    return bios