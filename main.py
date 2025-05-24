import requests
from bs4 import BeautifulSoup
import time

def verificar_amazon():
    print("🔍 Verificando Amazon Brasil...")

    url = "https://www.amazon.com.br/s?k=monitor+gamer"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        resultados = soup.select(".s-result-item")

        for item in resultados:
            titulo_tag = item.select_one("h2 a.a-link-normal")
            preco_tag = item.select_one(".a-price .a-offscreen")

            if titulo_tag and preco_tag:
                nome = titulo_tag.text.strip()
                link = "https://www.amazon.com.br" + titulo_tag['href']
                preco_text = preco_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".")
                preco = float(preco_text)

                if preco < 1000:
                    print(f"🔥 PROMO: {nome} - R${preco:.2f}")
                    print(f"🔗 Link: {link}\n")

    except Exception as e:
        print("Erro ao verificar Amazon:", e)

while True:
    verificar_amazon()
    time.sleep(3600)