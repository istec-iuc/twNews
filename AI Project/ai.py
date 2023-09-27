import requests
from bs4 import BeautifulSoup
from transformers import pipeline


def TextSummarizer(text, length):
    # Metni belirli bir maksimum uzunluğa kısaltın
    max_input_length = 1024  # Örnek olarak, maksimum giriş uzunluğunu 1024 olarak kabul ediyoruz
    text = text[:max_input_length - length]

    # Metni özetle
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", max_length=280 - length, min_length=150, do_sample=False)
    summary = summarizer(text)

    final_summary = summary[0]['summary_text']

    return final_summary


