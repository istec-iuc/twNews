from textblob import TextBlob

def TextBlob(metin):
    

    # Metin analizi için TextBlob'u kullanın
    analiz = TextBlob(metin)

    # Metnin duygu analizini alın
    duygu = analiz.sentiment

    # Duygu analizini yazdırın
    return "Duygu: {}, Güvenilirlik: {}".format(duygu.polarity, duygu.subjectivity)
