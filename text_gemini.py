import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def generate_gemini_response(prompt):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Please check your .env file.")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
