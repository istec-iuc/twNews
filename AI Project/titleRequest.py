import requests
from bs4 import BeautifulSoup

def WebRequestTitle(url):
    try:
        # Web sitesine erişim ve içeriği çekme
        response = requests.get(url)
        response.raise_for_status()  # Hata kontrolü
        html = response.text

        # HTML içeriğini analiz et
        soup = BeautifulSoup(html, "html.parser")

        # Haber başlığını bul
        title = soup.find("h1")  # Başlık h1 etiketinde ise
        if title:
            return title.text.strip()  # Başlığı temizle ve geri döndür

        # Başlık h1 etiketinde değilse, diğer olası etiketlere bakabilirsiniz, örneğin "h2" veya "h3".

        # Başlık bulunamadıysa, None döndürün
        return None

    except Exception as e:
        print("Hata:", e)
        return None