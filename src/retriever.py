from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chercher_chunks_pertinents(question, chunks, top_k=3):
    vectorizer = TfidfVectorizer()
    matrice = vectorizer.fit_transform(chunks)
    vecteur_question = vectorizer.transform([question])

    scores = cosine_similarity(vecteur_question, matrice)[0]

    indices_tries = scores.argsort()[::-1][:top_k]

    resultats = []
    for i in indices_tries:
        resultats.append((chunks[i], scores[i]))

    return resultats


if __name__ == "__main__":
    from loader import lire_pdf
    from chunker import decouper_en_chunks

    texte = lire_pdf("data/documents/cours SQL.pdf")
    chunks = decouper_en_chunks(texte)
    question = "Comment sélectionner toutes les colonnes ?"
    resultats = chercher_chunks_pertinents(question, chunks)

    for chunk, score in resultats:
        print(f"Score : {score:.3f}")
        print(chunk[:200])
        print("---")