def decouper_en_chunks(texte, taille=500, overlap=50):
    mots = texte.split()
    chunks = []
    pas = taille - overlap

    for debut in range(0, len(mots), pas):
        morceau = mots[debut:debut + taille]
        chunks.append(" ".join(morceau))

    return chunks


if __name__ == "__main__":
    from loader import lire_pdf

    texte = lire_pdf("data/documents/cours SQL.pdf")
    chunks = decouper_en_chunks(texte)
    print(f"Nombre de chunks : {len(chunks)}")
    print(f"Mots dans le chunk 0 : {len(chunks[0].split())}")
    print("--- Chunk 1 (début) ---")
    print(chunks[1][:300])
    print("--- Fin du chunk 0 ---")
    print(" ".join(chunks[0].split()[-10:]))
    print("--- Début du chunk 1 ---")
    print(" ".join(chunks[1].split()[:60]))
