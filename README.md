
# Outil de Recommandation de Films par Embeddings

## Introduction

Ce projet propose un outil de recommandation de films basé sur les **embeddings sémantiques** générés à partir des **synopsis** et **genres** de films. Il permet à un utilisateur de saisir un film et d’obtenir plusieurs suggestions de films similaires, grâce à un moteur intelligent utilisant le **modèle OpenAI `text-embedding-3-small`**.

Ce projet a été conçu dans un objectif d’apprentissage et de mise en pratique de techniques modernes en **scraping**, **traitement de texte**, **similarité cosinus**, **interface utilisateur avec Gradio**, et **traitement par lot parallèle**.

---

##  Fonctionnalités

### Embeddings sémantiques
Chaque film est transformé en un vecteur numérique basé sur son **synopsis + genres** via l'API d'OpenAI, pour permettre une mesure de similarité intelligente.

### Parallélisation (scraping rapide)
Le scraping des données depuis Allociné est parallélisé avec `ThreadPoolExecutor` pour accélérer le processus. Chaque page de film est extraite en simultané, ce qui permet d'accélérer le traitement des milliers de liens à parcourir.

### Traitement par batch (embeddings)
Les textes des films sont traités par **lots de 100**. Cela garantit à la fois efficacité et robustesse.

### Interface utilisateur (UI)
Une interface simple, intuitive et élégante est développée avec **Gradio**, permettant de :
- Saisir un titre de film.
- Choisir le nombre de recommandations à afficher.
- Obtenir les résultats avec **liens cliquables** vers Allociné.

---
## Comment utiliser l'outil ?

Vous avez deux options :

1. **Exécuter le code en local**, en suivant les étapes décrites dans la section [Installation & Utilisation](#️installation--utilisation).
2. **Utiliser l'outil directement en ligne** via l’interface hébergée sur Hugging Face :  
    [Accéder à la démo en ligne](https://huggingface.co/spaces/aymanexv/Outildesuggestiondefilm)


## Installation & Utilisation

### Pré-requis
- Python 3.8+
- Une clé API OpenAI ([créer ici](https://platform.openai.com/account/api-keys))
- Packages : `pandas`, `numpy`, `openai`, `scikit-learn`, `gradio`, `beautifulsoup4`, `requests`
- Télécharger les donnée via ce lien :  ([créer ici]
  (https://drive.google.com/drive/folders/1g2advXkIDeL_xDou16z9LaalyiGJMeuz))

### Étapes d’installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/outil-suggestion-film.git
cd outil-suggestion-film

# 2. Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

###  Étape 1 - Scraping des films

Dans `scrapping.py` :
```bash
python scrapping.py
```
Cela génère un fichier `films.csv` avec les titres, synopsis, genres, liens.

###  Étape 2 - Génération des embeddings

Dans `embeddings.py` :
- Remplacer la ligne `openai.api_key = "Mettre votre clé API OpenAI"` par votre propre clé API.
- Modifier le chemin d’accès au CSV si besoin.

Puis exécuter :
```bash
python embeddings.py
```
Cela ajoute les vecteurs d’embeddings dans le fichier `films.csv`.

### 🌐 Étape 3 - Lancer l’interface utilisateur

Dans `app.py` :
```bash
python app.py
```
Une interface Gradio s’ouvre dans votre navigateur. Entrez un film, obtenez des recommandations !

---

## Données

Les données utilisées dans ce projet proviennent d’**Allociné** via web scraping. Si vous souhaitez éviter les longues phases de scraping et d'embedding, vous pouvez télécharger un fichier `films.csv` déjà prêt (embeddings inclus) ici :

🔗 **[Lien Google Drive (à ajouter)](https://drive.google.com/...)**

Placez ce fichier dans le dossier du projet avant d'exécuter `app.py`.

---

##  Structure du projet

```
outil-suggestion-film/
│
├── scrapping.py                # Scraping des films depuis Allociné
├── embeddings.py               # Génération des embeddings OpenAI
├── recommandation_cosine_similarity.py # Fonction de recommandation
├── app.py                      # Interface utilisateur Gradio
├── films.csv                   # Données enrichies (synopsis, genres, embeddings)
├── requirements.txt            # Fichier de dépendances
└── README.md                   # Documentation du projet
```
---

## Auteurs

- **Aymane AIBICHI** — [@aymanevx](https://github.com/aymanevx)
- **Zineb MANAR** — [@ZinebMnr](https://github.com/ZinebMnr)
- **Anass Azeggouarh Wallen** — [@AnassAzeggouarh](https://github.com/AnassAzeggouarh)
