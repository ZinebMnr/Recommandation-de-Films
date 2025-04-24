import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommander(titre_film, df, top_k=3):
    if titre_film not in df["name"].values:
        print("Film non trouvé.")
        return None

    index = df[df["name"] == titre_film].index[0]
    emb = np.array(df.loc[index, "embedding"]).reshape(1, -1)
    all_embs = np.vstack(df["embedding"].values)
    sims = cosine_similarity(emb, all_embs)[0]

    df["similarité"] = sims
    reco = df[df["name"] != titre_film].sort_values(by="similarité", ascending=False)
    return reco[["name", "genre", "similarité", "link"]].head(top_k)

recommandations = recommander("nom du film", df)
print(recommandations)
