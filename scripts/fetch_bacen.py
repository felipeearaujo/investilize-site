import requests
import json
import os

def sync_bacen():
    # Código 432: Selic Meta (Dados Oficiais do Banco Central)
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json"
    
    try:
        print("Consultando Banco Central...")
        response = requests.get(url, timeout=10)
        selic_valor = response.json()[0]['valor']
        
        # Garante que a pasta src/data existe
        os.makedirs('src/data', exist_ok=True)
        
        # Salva o resultado
        with open('src/data/bacen.json', 'w', encoding='utf-8') as f:
            json.dump({"selic": selic_valor}, f)
            
        print(f"✅ Sucesso! Selic de {selic_valor}% salva para o Astro.")
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

if __name__ == "__main__":
    sync_bacen()