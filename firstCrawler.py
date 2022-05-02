from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen
from htmlParser import Collector

class Crawler(object):


    def init(self):
        self.visited = set()

    def reset(self):
        self.visited = []

    def crawl(self, url):
        links = self.analyze(url)
        self.visited.add(url)
        for link in links:
            try:
                if link not in self.visited:
                    self.crawl(link)
            except:
                pass

    def analyze(self, url):
        print("currently at: ", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls


