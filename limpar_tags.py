# -*- coding: utf-8 -*-
import os
import re

REPO_PATH = "/root/investilize-site"
PASTA_NOTICIAS = os.path.join(REPO_PATH, "src/pages/noticias")

print("--- 🧹 Iniciando limpeza de tags órfãs ---")

for arquivo in os.listdir(PASTA_NOTICIAS):
    if arquivo.endswith(".md"):
        caminho_md = os.path.join(PASTA_NOTICIAS, arquivo)
        
        with open(caminho_md, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # 1. Remove o bloco do link da Agência Brasil que ficou vazio (sem a imagem)
        # Procura pelo padrão <p...><a...> e o que sobrou dele
        novo_conteudo = re.sub(r'<p style="text-align: center;">\s*<a[^>]*>\s*</a>\s*</p>', '', conteudo)
        
        # 2. Caso tenha sobrado apenas o fechamento (o erro que você viu)
        novo_conteudo = novo_conteudo.replace('</a></p>', '')
        
        # 3. Limpa espaços duplos que podem ter surgido
        novo_conteudo = novo_conteudo.replace('\n\n\n', '\n\n')

        if novo_conteudo != conteudo:
            with open(caminho_md, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            print(f"✨ Limpo: {arquivo}")

print("--- ✅ Notícias higienizadas! ---")