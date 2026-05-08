import os
import re

path = 'src/content/noticias/'

for filename in os.listdir(path):
    if filename.endswith(".md"):
        filepath = os.path.join(path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verifica se já existe o campo description
        if 'description:' not in content:
            # Busca o título (com aspas simples, duplas ou sem aspas)
            title_match = re.search(r"title:\s*['\"]?(.*?)['\"]?\n", content)
            if title_match:
                title = title_match.group(1)
                # Cria a descrição otimizada para o Google
                desc_line = f"description: 'Saiba mais sobre {title}. Acompanhe as principais notícias do mercado financeiro no Investilize.'\n"
                
                # Insere logo abaixo do título
                new_content = re.sub(r"(title:.*\n)", r"\1" + desc_line, content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Campo description injetado em: {filename}")