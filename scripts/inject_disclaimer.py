import os
import glob

# The calculators we want to add the disclaimer to
calculators = [
    "CalculadoraIRMensal.astro",
    "CalculadoraJuros.astro",
    "CalculadoraPrecoJusto.astro",
    "CalculadoraTaxaReal.astro",
    "ComparadorRendaFixa.astro",
    "ConversorMoedas.astro",
    "CotacaoAcoes.astro",
    "IndependenciaFinanceira.astro",
    "PoderCompra.astro",
    "ReservaEmergencia.astro",
    "SimuladorPerfil.astro",
    "Taxometro.astro",
    "TesouroVsBancao.astro"
]

comp_dir = 'src/components/ferramentas'

for calc in calculators:
    path = os.path.join(comp_dir, calc)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'Disclaimer' in content:
        continue
        
    # Insert import
    if '---\n' in content:
        content = content.replace("---\n", "---\nimport Disclaimer from '../Disclaimer.astro';\n", 1)
    else:
        content = "---\nimport Disclaimer from '../Disclaimer.astro';\n---\n" + content
        
    # Insert <Disclaimer /> before the first <script> or <style>
    if '<script>' in content:
        content = content.replace("<script>", "<Disclaimer />\n\n<script>")
    elif '<style>' in content:
        content = content.replace("<style>", "<Disclaimer />\n\n<style>")
    else:
        content += "\n<Disclaimer />"
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Disclaimer injected successfully!")
