import os
import glob

# The pages to update
files_to_update = [
    "independencia-financeira.astro",
    "calculadora-preco-justo.astro",
    "juros-compostos.astro",
    "conversor-de-moedas.astro",
    "calculadora-reserva-emergencia.astro",
    "comparador-renda-fixa.astro"
]

pages_dir = 'src/pages/ferramentas'

for file_name in files_to_update:
    path = os.path.join(pages_dir, file_name)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the @type value
    old_str = '"@type": "SoftwareApplication",'
    new_str = '"@type": ["SoftwareApplication", "FinancialProduct"],'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Schema updated successfully in 6 files!")
