from twitter import *
from ai import *
from request import *
from titleRequest import *
from getrss import *
from translate import *
from textBlob import *
import sqlite3
from datetime import datetime

url=input('Web sayfasının url\'ini giriniz : ')
kaynak=input("haber kaynağı : ")
links=getRss(url)

for link in links:
    text1=WebRequest(link)
    title=WebRequestTitle(link)
    length=len(title)+len(kaynak)+8+2

    text_summaries=TextSummarizer(text1,length)
    text_summaries=title+"->"+text_summaries
    if len(text_summaries)>280-length:
        text_summaries=text_summaries[0:280-length-3]+"..."
    translateText=translate_text(text_summaries,"tr")
    try:
        SendTwitter(translateText,kaynak)
    except:
        continue
    sharedHistory=datetime.now()


    # database connection
    conn=sqlite3.connect("C:\\Users\\yusuf\\OneDrive\\Masaüstü\\AI Project\\istechaber.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS News (
                        id INTEGER PRIMARY KEY,
                        url TEXT,
                        title TEXT,
                        content TEXT,
                        source TEXT,
                        sharedHistory TEXT
                    )''')
    cursor.execute("INSERT INTO News (url, title, content, source, sharedHistory) VALUES (?, ?, ?, ?, ?)",(url, title, text_summaries, kaynak,str(sharedHistory)))

    conn.commit()
    # Bağlantıyı kapatın.
    conn.close()
