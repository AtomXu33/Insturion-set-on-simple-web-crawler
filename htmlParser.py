from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urlparse

def Parser(url):
    content = urlopen(url).read().decode()
    parser = Collector(url)
    parser.feed(content)
    return parser.getLinks()


class HeaderParser(HTMLParser):

    def init(self):
        HTMLParser.init(self)
        self.lst = list()
        self.inHeading = False

    def getHeadings(self):
        return self.lst

    def handle_starttag(self ,tag, attrs):
        if tag.lower() in ["h1","h2","h3","h4","h5","h6"]:
            self.inHeading = True

    def handle_endtag(self, tag):
        if tag.lower() in ["h1","h2","h3","h4","h5","h6"]:
            self.inHeading = False

    def handle_data(self,data):
        if self.inHeading == True:
            self.lst.append(data.strip())


class DataCollector(HTMLParser):

    def init(self):
        HTMLParser.init(self)
        self.contents = ""

    def getData(self):
        return self.contents

    def handle_data(self,data):
        data1 = data.strip()
        if len(data1) > 0 :
            data1 += "\n"
            self.contents += data1



class Collector(HTMLParser):


    def init(self,url):
        HTMLParser.init(self)
        self.lst = list()
        self.url = url

    def getLinks(self):
        return self.lst

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for item in attrs:
                if item[0].lower() == 'href':
                    self.lst.append(urljoin(self.url,item[1]))



