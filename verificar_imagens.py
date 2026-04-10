# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

# Caminho das noticias no seu Astro
pasta = "src/pages/noticias"

def limpar_url_ebc(url):
    """Remove o prefixo do seu site se o bot tiver salvo o link duplicado."""
    if "http" in url:
        # Pega apenas a partir do último 'http' encontrado para limpar lixo de thumbnails
        pos = url.rfind("http")
        return url[pos:]
    return url

def pegar_imagem_fresca(url):
    """Busca a imagem original direto na fonte (Agência Brasil)."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Prioriza metadados que são URLs absolutas e limpas
        tag = soup.find("meta", property="og:image") or soup.find("meta", attrs={"name": "twitter:image"})
        if tag and tag.get("content"):
            return limpar_url_ebc(tag.get("content"))

        # Backup: busca no corpo do texto tratando lazy load
        img_artigo = soup.select_one("article img, main img")
        if img_artigo:
            src = img_artigo.get("data-src") or img_artigo.get("src")
            return urljoin(url, src)
    except:
        pass
    return None

print("--- 🚀 Iniciando Varredura Automática ---")

for root, dirs, files in os.walk(pasta):
    for file in files:
        if file.endswith(".md"):
            caminho = os.path.join(root, file)
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            # Identifica se a imagem está quebrada (GIF ou link duplicado)
            if "loading_v2.gif" in conteudo or "investilize.com.br/sites/" in conteudo:
                match = re.search(r'originalUrl:\s*"([^"]+)"', conteudo)
                if match:
                    url_fonte = match.group(1)
                    nova_img = pegar_imagem_fresca(url_fonte)
                    
                    if nova_img:
                        # Corrige no Frontmatter (heroImage) e no corpo do texto (img tag)
                        conteudo = re.sub(r'heroImage:\s*"[^"]*"', f'heroImage: "{nova_img}"', conteudo)
                        conteudo = re.sub(r'src="[^"]*loading_v2\.gif"', f'src="{nova_img}"', conteudo)
                        
                        with open(caminho, "w", encoding="utf-8") as f:
                            f.write(conteudo)
                        print(f"✅ {file} corrigido!")

print("--- ✨ Todas as notícias antigas foram limpas! ---")