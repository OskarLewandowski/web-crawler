from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print(tag)

    def error(self, message):
        pass
