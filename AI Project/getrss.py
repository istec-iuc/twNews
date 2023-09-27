import feedparser

def getRss(rssUrl):
    rss_url = rssUrl
    feed = feedparser.parse(rss_url)
    liks=list()
    for entry in feed.entries:
        # title = entry.title
        link = entry.link
        # description = entry.description
        # print(title)
        # print(link)
        # print(description)
        # Diğer gerekli bilgileri de burada alabilirsiniz
        liks.append(link)
    return liks