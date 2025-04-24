import numpy as np 
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr
import ast

# Charger le DataFrame
df = pd.read_csv("films.csv")
df["embedding"] = df["embedding"].apply(ast.literal_eval)

# Fonction de recommandation
def recommander(titre_film, top_k=3):
    if titre_film not in df["name"].values:
        return f"❌ Film '{titre_film}' non trouvé.", ""

    index = df[df["name"] == titre_film].index[0]
    emb = np.array(df.loc[index, "embedding"]).reshape(1, -1)
    all_embs = np.vstack(df["embedding"].values)
    sims = cosine_similarity(emb, all_embs)[0]

    df["similarité"] = sims
    reco = df[df["name"] != titre_film].sort_values(by="similarité", ascending=False)
    recommandations = reco[["name", "genre", "similarité", "link"]].head(top_k)

    # Générer une sortie en Markdown avec des liens cliquables
    markdown_result = f"### 🎬 Recommandations pour **{titre_film}** :\n"
    for _, row in recommandations.iterrows():
        markdown_result += f"- [{row['name']} ({row['genre']}) - Similarité : {row['similarité']:.2f}]({row['link']})\n"

    return "", markdown_result

# Interface Gradio
interface = gr.Interface(
    fn=recommander,
    inputs=[
        gr.Textbox(label="Titre du film"),
        gr.Slider(minimum=1, maximum=10, value=3, step=1, label="Nombre de recommandations")
    ],
    outputs=[
        gr.Textbox(label="Message"),
        gr.Markdown(label="Films recommandés")  # Markdown pour gérer les liens
    ],
    title="Recommandation de films",
    description="Entre un titre de film pour voir les suggestions basées sur les embeddings (avec liens cliquables)."
)

# Lancer l'interface
interface.launch()