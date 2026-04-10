# -*- coding: utf-8 -*-
import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Configurações do seu ambiente
REPO_PATH = "/root/investilize-site"
PASTA_MD = os.path.join(REPO_PATH, "src/pages/noticias")
PASTA_IMG = os.path.join(REPO_PATH, "public/images/noticias")

# Cria a pasta de imagens se não existir
os.makedirs(PASTA_IMG, exist_ok=True)

def extrair_imagem_da_fonte(url_noticia):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url_noticia, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Procura a imagem real nos metadados da Agência Brasil
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            return urljoin(url_noticia, og.get("content"))
    except:
        pass
    return None

print(f"--- 🚀 Iniciando Varredura em {PASTA_MD} ---")

# Lista todos os arquivos que o grep encontraria
arquivos = [f for f in os.listdir(PASTA_MD) if f.endswith(".md")]

for arquivo in arquivos:
    caminho_completo = os.path.join(PASTA_MD, arquivo)
    slug = arquivo.replace(".md", "")
    
    with open(caminho_completo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Se o arquivo tem o link quebrado ou o gif de loading
    if "/sites/" in conteudo or "loading" in conteudo:
        print(f"📦 Corrigindo: {arquivo}")
        
        # 1. Busca a URL original para saber de onde baixar a foto real
        match = re.search(r'originalUrl:\s*"([^"]+)"', conteudo)
        if match:
            url_fonte = match.group(1)
            url_foto_real = extrair_imagem_da_fonte(url_fonte)
            
            if url_foto_real:
                # 2. Faz o download da foto para o seu servidor
                try:
                    r_img = requests.get(url_foto_real, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                    if r_img.status_code == 200:
                        nome_img = f"{slug}.jpg"
                        with open(os.path.join(PASTA_IMG, nome_img), 'wb') as f_img:
                            f_img.write(r_img.content)
                        
                        # 3. ATUALIZA O CONTEÚDO
                        caminho_local = f"/images/noticias/{nome_img}"
                        
                        # Troca o heroImage
                        conteudo = re.sub(r'heroImage:\s*"[^"]*"', f'heroImage: "{caminho_local}"', conteudo)
                        
                        # Remove a tag <img> duplicada que o bot antigo inseria no corpo
                        conteudo = re.sub(r'<img[^>]*>', '', conteudo)
                        
                        with open(caminho_completo, "w", encoding="utf-8") as f_out:
                            f_out.write(conteudo)
                        
                        print(f"   ✅ Imagem baixada e Markdown limpo!")
                except Exception as e:
                    print(f"   ❌ Erro ao baixar imagem: {e}")
        else:
            print(f"   ⚠️ 'originalUrl' não encontrado no arquivo.")

print("--- ✨ Processo concluído! ---")