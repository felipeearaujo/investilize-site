# -*- coding: utf-8 -*-
import os
import re

pasta = "src/pages/noticias"

print("--- 🧹 Iniciando Limpeza de URLs Frankenstein ---")

for root, dirs, files in os.walk(pasta):
    for file in files:
        if file.endswith(".md"):
            caminho = os.path.join(root, file)
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            # Procura por qualquer URL que tenha "http" grudado no caminho local
            if "/sites/" in conteudo and "http" in conteudo:
                # Regex que identifica o lixo antes do http e remove
                novo_conteudo = re.sub(r'\/sites\/[^"]*http', 'http', conteudo)
                
                if novo_conteudo != conteudo:
                    with open(caminho, "w", encoding="utf-8") as f:
                        f.write(novo_conteudo)
                    print(f"✅ Limpo: {file}")

print("--- ✨ Limpeza concluída! ---")