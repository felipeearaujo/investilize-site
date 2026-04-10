# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

# Caminho da pasta onde esto os arquivos .md no seu servidor
pasta = "src/pages/noticias"

def pegar_imagem(url):
    try:
        # Adicionamos um cabealho para parecer um navegador real
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "html.parser")

        # 1. Tenta og:image (melhor qualidade)
        tag = soup.find("meta", property="og:image") or soup.find("meta", attrs={"name": "twitter:image"})
        
        if tag and tag.get("content"):
            img_url = tag.get("content")
            # Converte links relativos em absolutos automaticamente
            return urljoin(url, img_url)

        # 2. Backup: busca a primeira imagem do artigo se no tiver meta tag
        img_artigo = soup.select_one("article img, main img")
        if img_artigo:
            src = img_artigo.get("data-src") or img_artigo.get("src")
            return urljoin(url, src)

    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

    return None

# Varredura dos arquivos
for root, dirs, files in os.walk(pasta):
    for file in files:
        if file.endswith(".md"):
            caminho = os.path.join(root, file)

            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            # Verifica se o arquivo contm o GIF de loading ou o caminho quebrado
            if "loading_v2.gif" in conteudo:
                print(f"--- Corrigindo: {file} ---")

                # Encontra a URL original no Frontmatter
                match = re.search(r'originalUrl:\s*"([^"]+)"', conteudo)

                if match:
                    url_original = match.group(1)
                    nova_imagem = pegar_imagem(url_original)

                    if nova_imagem:
                        # Substitui a imagem antiga (ou o link do carregamento) pela nova
                        # Usamos regex para encontrar o campo heroImage: "..." e substituir
                        conteudo = re.sub(r'heroImage:\s*"[^"]*"', f'heroImage: "{nova_imagem}"', conteudo)
                        
                        # Se voc tambm tiver a imagem dentro do corpo do texto (tag <img>)
                        conteudo = conteudo.replace("loading_v2.gif", nova_imagem)

                        with open(caminho, "w", encoding="utf-8") as f:
                            f.write(conteudo)

                        print(f"? Sucesso! Nova imagem: {nova_imagem}")
                    else:
                print(f"[-] Imagem real nao encontrada para: {url_original}")o encontrada para: {url_original}")
                else:
                    print(f"?? Campo 'originalUrl' no encontrado no arquivo {file}")

print("\n? Varredura concluda!")