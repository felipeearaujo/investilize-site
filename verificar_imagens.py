import requests
from bs4 import BeautifulSoup
import os
import re

pasta = "src/pages/noticias"

def pegar_imagem(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # procurar og:image
        tag = soup.find("meta", property="og:image")

        if tag:
            return tag.get("content")

    except Exception as e:
        print("Erro ao acessar:", url)

    return None


for root, dirs, files in os.walk(pasta):

    for file in files:

        if file.endswith(".md"):

            caminho = os.path.join(root, file)

            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            if "loading_v2.gif" in conteudo:

                print("Corrigindo:", file)

                # encontrar url original
                match = re.search(r'originalUrl:\s*"([^"]+)"', conteudo)

                if match:

                    url = match.group(1)

                    imagem = pegar_imagem(url)

                    if imagem:

                        conteudo = conteudo.replace(
                            "loading_v2.gif",
                            imagem
                        )

                        with open(caminho, "w", encoding="utf-8") as f:
                            f.write(conteudo)

                        print("Imagem corrigida:", imagem)

                    else:

                        print("Imagem não encontrada:", url)