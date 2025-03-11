from typing import List, Dict
import google.generativeai as genai  # Using Gemini API
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_bio(user_text: str) -> List[Dict[str, str]]:
    prompts = [
        "You are a professional bio writer. Generate a detailed, formal bio.",
        "You are a creative writer. Generate a bio with a friendly and approachable tone.",
        "You are a marketing expert. Generate a bio that highlights achievements and expertise.",
        "You are a storyteller. Generate a bio that feels like a personal story."
    ]
    
    bios = []
    model = genai.GenerativeModel("gemini-2.0-flash")
    for i, prompt in enumerate(prompts, 1):
        response = model.generate_content(f"{prompt}\nGenerate a bio based on the following text: {user_text}")
        bios.append({"id": i, "content": response.text})
    
    return bios# Updated script
