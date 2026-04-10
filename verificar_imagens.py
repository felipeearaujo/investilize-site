import os
import requests
from bs4 import BeautifulSoup

PASTA = "src/pages/noticias"

def pegar_imagem_real(url):

    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")

        # 1️⃣ OG IMAGE
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            return og.get("content")

        # 2️⃣ TWITTER IMAGE
        tw = soup.find("meta", attrs={"name": "twitter:image"})
        if tw and tw.get("content"):
            return tw.get("content")

        # 3️⃣ IMAGEM DO ARTIGO
        imgs = soup.select("article img, main img")

        for img in imgs:
            src = (
                img.get("data-src")
                or img.get("data-echo")
                or img.get("data-original")
                or img.get("src")
            )

            if not src:
                continue

            if "loading" in src or ".gif" in src:
                continue

            return src

    except Exception as e:
        print("Erro ao acessar:", url)

    return None


for root, dirs, files in os.walk(PASTA):

    for file in files:

        if not file.endswith(".md"):
            continue

        caminho = os.path.join(root, file)

        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()

        if "loading_v2.gif" not in conteudo:
            continue

        print("Corrigindo:", file)

        # procurar originalUrl
        url = None

        for linha in conteudo.split("\n"):
            if "originalUrl:" in linha:
                url = linha.replace("originalUrl:", "").strip().replace('"', '').replace("'", "")
                break

        if not url:
            print("URL original não encontrada")
            continue

        imagem = pegar_imagem_real(url)

        if not imagem:
            print("Imagem não encontrada:", url)
            continue

        conteudo_novo = conteudo.replace("loading_v2.gif", imagem)

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo_novo)

        print("Imagem corrigida:", imagem)