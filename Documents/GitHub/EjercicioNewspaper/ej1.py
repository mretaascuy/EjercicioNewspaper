import re
from collections import Counter


def body(url):
    from newspaper import Article
    #url = 'https://www.nytimes.com/2016/08/07/education/edlife/kenneth-goldsmith-on-wasting-time-on-the-internet.html'
    article = Article(url)
    article.download()
    article.parse()
    articulo= article.text
    lista= re.split(r'\W+', articulo)
    d=Counter(lista)
    return d