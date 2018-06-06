import urllib2
from bs4 import BeautifulSoup
from stop_words import get_stop_words
from db_connection import DBConnection
import unicodedata


class Scrapper:

    def __init__(self, url):
        self.URL = url
        self.dataSplited = list()
        self.dictOfWords = {}
        self.data = None

    def parse_data(self):
        stop_words = get_stop_words('spanish')

        for word in self.data.split(" "):
            uniInput = unicode(word, encoding='utf-8')
            uniInput = uniInput.replace(".", "")
            uniInput = uniInput.replace(",", "")
            # print type(uniInput)
            a = uniInput.encode("utf-8")
            if a not in stop_words and a is not "" and a is not " ":
                if a not in self.dictOfWords:
                    self.dictOfWords[a] = 1
                else:
                    self.dictOfWords[a] += 1

    def get_data(self, lines=1000):
        if (self.URL.endswith('.txt')):
            # parseo los datos y los subo
            self.data = urllib2.urlopen(str(self.URL)).read(lines)

            self.data = self.data.replace("\n", " ")
