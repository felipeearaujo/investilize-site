import requests
import json
import os

def fetch_ipca_completo():
    # Série 433: IPCA mensal (%)
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
    
    try:
        print("Baixando histórico completo do IPCA...")
        response = requests.get(url, timeout=30)
        data = response.json()
        
        # Estruturamos os dados para busca rápida no Astro: { "MM/AAAA": valor }
        ipca_map = {item['data']: float(item['valor']) for item in data}
        
        os.makedirs('src/data', exist_ok=True)
        with open('src/data/ipca_historico.json', 'w') as f:
            json.dump(ipca_map, f)
            
        print(f"✅ Sucesso! {len(ipca_map)} meses de IPCA salvos.")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    fetch_ipca_completo()