import requests
import xml.etree.ElementTree as ET

# 🔑 Configurações
HOST = "investilize.com.br"
KEY = "2eb7f0f1032645eda06d803bd8ca124e"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
SITEMAP_URL = "https://investilize.com.br/sitemap.xml"  # coloque o link do seu sitemap

def get_urls_from_sitemap(sitemap_url):
    """Lê o sitemap XML e retorna uma lista de URLs"""
    response = requests.get(sitemap_url)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    # O namespace do sitemap precisa ser tratado
    namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [url.text for url in root.findall(".//ns:loc", namespace)]
    return urls

def send_to_indexnow(urls):
    """Envia as URLs para o IndexNow"""
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    response = requests.post("https://api.indexnow.org/IndexNow", json=payload)
    print("Status:", response.status_code)
    print("Resposta:", response.text)

def main():
    print("🔍 Lendo sitemap...")
    urls = get_urls_from_sitemap(SITEMAP_URL)
    print(f"Encontradas {len(urls)} URLs")

    # ⚡ envia em lotes de até 10.000 (limite do IndexNow)
    send_to_indexnow(urls)

if __name__ == "__main__":
    main()
