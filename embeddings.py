import openai
import pandas as pd
import numpy as np

openai.api_key = "Mettre votre clé API OpenAI"
# Remplace "chemin d'accès" par le chemin réel de ton fichier CSV
df = pd.read_csv("Chemin d'accès")
# Supprime les doublons sur la colonne 'name'
df = df.drop_duplicates(subset='name', keep='first')

def embed_batch(texts, model="text-embedding-3-small"):
    response = openai.embeddings.create(
        input=texts,
        model=model
    )
    return [r.embedding for r in response.data]

# Préparer les textes
df["texte"] = df["synopsis"].fillna("") + " Genres : " + df["genre"].fillna("")
df["texte"] = df["texte"].astype(str)
df["texte"] = df["texte"].apply(lambda x: x[:4000])  # éviter dépassement de tokens

# Initialiser une liste pour stocker les embeddings
all_embeddings = []

# Découper en paquets de 100 textes
batch_size = 100
for i in range(0, len(df), batch_size):
    batch_texts = df["texte"].iloc[i:i+batch_size].tolist()
    try:
        batch_embeddings = embed_batch(batch_texts)
        all_embeddings.extend(batch_embeddings)
    except Exception as e:
        print(f"Erreur au batch {i}-{i+batch_size}: {e}")

# Ajouter les embeddings au DataFrame
if len(all_embeddings) == len(df):
    df["embedding"] = all_embeddings
else:
    print("Erreur : le nombre d'embeddings ne correspond pas au nombre de lignes.")

df.to_csv("films.csv", index=False, encoding="utf-8-sig")





