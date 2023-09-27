import requests
from bs4 import BeautifulSoup

def WebRequest(url):
    # Web sitesine erişim ve makaleyi çekme
    # url = input("Özetlemek istediğiniz makalenin URL'sini girin: ")
    response = requests.get(url)
    html = response.text

    # HTML içeriği analiz edin
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1")
    paragraphs = soup.find_all("p")  # Metin genellikle <p> etiketleri içinde bulunur
    return " ".join([p.get_text() for p in paragraphs])