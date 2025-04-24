import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from concurrent.futures import ThreadPoolExecutor

headers = {"User-Agent": "Mozilla/5.0"}

def get_film_links(page):
    url = f"https://www.allocine.fr/films/?page={page}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    links = [
        "https://www.allocine.fr" + a["href"]
        for a in soup.select("h2.meta-title a.meta-title-link")
        if a.get("href")
    ]
    return links

def get_film_info(link):
    try:
        resp_f = requests.get(link, headers=headers)
        resp_f.raise_for_status()
        fsoup = BeautifulSoup(resp_f.text, "html.parser")

        # Titre
        film_name = (
            fsoup.title.string.split(" - ")[0].strip()
            if fsoup.title and fsoup.title.string
            else None
        )

        # Synopsis
        syno_el = fsoup.select_one(".content-txt")
        film_synopsis = syno_el.get_text(strip=True) if syno_el else None

        # Genre(s)
        genre = None
        json_ld = fsoup.find("script", type="application/ld+json")
        if json_ld and json_ld.string:
            try:
                data = json.loads(json_ld.string)
                genre_data = data.get("genre")
                if isinstance(genre_data, list):
                    genre = ", ".join(genre_data)
                elif isinstance(genre_data, str):
                    genre = genre_data
            except json.JSONDecodeError:
                genre = None

        return {
            "name": film_name,
            "synopsis": film_synopsis,
            "genre": genre,
            "link": link  #  Ajout du lien ici
        }

    except Exception as e:
        print(f"Erreur pour {link}: {e}")
        return None

def grab_info_parallel(total_pages=3, max_workers=10):
    print(f"Scraping les pages de liste (1 à {total_pages})...")
    all_links = []

    for page in range(1, total_pages + 1):
        links = get_film_links(page)
        print(f" → Page {page} : {len(links)} films trouvés.")
        all_links.extend(links)

    print(f"\n→ Total films à scraper : {len(all_links)}")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(get_film_info, all_links))

    results = [film for film in results if film is not None]
    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    df = grab_info_parallel(total_pages=1400, max_workers=15)
    print(df.head())

    df.to_csv("films.csv", index=False, encoding="utf-8-sig")
    print("→ CSV créé : films.csv")
