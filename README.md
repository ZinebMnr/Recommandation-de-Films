# Recommandation de Films

Bienvenue dans notre projet de recommandation de films basé sur les synopsis ! À partir d'un simple titre de film en entrée, notre application vous propose une sélection de films similaires, avec les liens AlloCiné à portée de clic.

**Tester l'application ici** : [Outil de suggestion de films (Hugging Face)](https://huggingface.co/spaces/aymanexv/Outildesuggestiondefilm)

---

## Membres du projet

Ce projet a été réalisé dans le cadre de notre master par :

- **Zineb Manar**
- **Aymane Aibichi**
- **Anass**

---

## Fonctionnalités principales

- Entrée libre d’un **titre de film**
- Sélection du **nombre de recommandations** à afficher
- Recommandations basées sur la **similarité sémantique** des synopsis
- Affichage des **liens directs vers les fiches AlloCiné** pour chaque film suggéré

---

## Pipeline du projet

Le projet est structuré en **trois grandes étapes** :

### 1. Scraping des films

- Source : [AlloCiné](https://www.allocine.fr)
- Environ **20 000 films** récupérés
- Scraping par lots de **15 films par page**, sur plusieurs centaines de pages
- Données collectées : titre, synopsis, genres et lien vers la fiche AlloCiné

### 2. Embedding des synopsis

- Utilisation de l’**API OpenAI (ChatGPT)** pour vectoriser les synopsis
- Calcul de la **similarité cosinus** pour déterminer les films les plus proches

### 3. Interface utilisateur

- Développée avec **Hugging Face Spaces**
- Saisie du titre de film + choix du nombre de recommandations
- Affichage instantané des suggestions avec leurs **titres et liens AlloCiné**

---

## Technologies utilisées

- `Python` : BeautifulSoup, requests, pandas, numpy
- `OpenAI API` : embeddings de textes
- `Hugging Face Spaces` : hébergement de l’interface
- `Jupyter Notebook` : développement initial

---

## Testez le !

Lien vers l'interface : https://huggingface.co/spaces/aymanexv/Outildesuggestiondefilm

![Capture d'écran 2025-04-24 193912](https://github.com/user-attachments/assets/835ed992-74b8-47ad-b0de-299b57009963)

