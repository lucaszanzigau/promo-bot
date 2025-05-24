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
            titulo = item.select_one("h2 span")
            preco = item.select_one(".a-price .a-offscreen")

            if titulo and preco:
                nome = titulo.text.strip()
                valor = preco.text.strip().replace("R$", "").replace(".", "").replace(",", ".")
                valor_float = float(valor)

                if valor_float < 1000:  # valor de corte para promoção
                    print(f"🔥 PROMO: {nome} - R${valor_float:.2f}")

    except Exception as e:
        print("Erro ao verificar Amazon:", e)

while True:
    verificar_amazon()
    time.sleep(3600)