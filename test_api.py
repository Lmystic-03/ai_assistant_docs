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
from pypdf import PdfReader

def lire_pdf(chemin):
    lecteur = PdfReader(chemin)
    texte = ""
    for page in lecteur.pages:
        texte += page.extract_text() + "\n"
    return texte
if __name__ == "__main__":
    texte = lire_pdf("data/documents/cours SQL.pdf")
    print(f"Nombre de caractères : {len(texte)}")
    print(texte[:500])