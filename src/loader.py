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