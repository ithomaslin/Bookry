import requests
import lxml
import re
import sys
from pyquery import PyQuery


BASE_URL = 'http://www.books.com.tw/web/books'


def chinese_books_category_url(url):
    urls = []
    try:
        res = requests.get(url)
        s = PyQuery(res.text)
        urls = s("ul > li > span > a").map(lambda i, el: PyQuery(el).attr("href"))
    except sys.exc_info():
        print sys.exc_info()[0]

    return urls


def chinese_books_sub_category_url(urls):
    sub_urls = []
    for url in urls:
        try:
            res = requests.get(url)
            s = PyQuery(res.text)
            urls = s("ul.sub > li > span > a").map(lambda i, el: PyQuery(el).attr("href"))
            sub_urls = sub_urls+urls
        except sys.exc_info():
            print sys.exc_info()[0]

    return sub_urls


