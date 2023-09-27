import requests

def translate_text(text, target_language):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_language}"
    response = requests.get(url)
    data = response.json()
    
    if "responseStatus" in data and data["responseStatus"] == 200:
        return data["responseData"]["translatedText"]
    else:
        return "Çeviri yapılamadı."