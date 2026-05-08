import os

dirs = ['src/content/blog/', 'src/content/noticias/']

print("🧹 Corrigindo conflito YAML vs LaTeX no Frontmatter...")

for d in dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        if f.endswith(('.md', '.mdx')):
            path = os.path.join(d, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Divide o arquivo pelos delimitadores do Frontmatter ---
            parts = content.split('---')
            if len(parts) >= 3:
                # parts[1] é o conteúdo do Frontmatter (YAML)
                yaml_block = parts[1]
                # Removemos os escapes que irritam o YAML
                yaml_block = yaml_block.replace(r'\$', '$').replace(r'\%', '%')
                
                # Remontamos o arquivo
                new_content = '---' + yaml_block + '---' + '---'.join(parts[2:])
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"✅ Frontmatter limpo: {f}")

print("🏁 Agora o YAML está feliz. Tente o build novamente!")