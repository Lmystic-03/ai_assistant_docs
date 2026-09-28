import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explique la régression linéaire.",
    config=types.GenerateContentConfig(
        system_instruction="Tu es un assistant qui répond en français, de manière concise, en 2 phrases maximum.",
        temperature=0.2,
    ),
)

print(response.text)