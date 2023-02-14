import urllib.request
from link_finder import LinkFinder
from general import *
from domain import *
from bs4 import BeautifulSoup
import requests


class Spider:
    # Class variables
    project_name = ""
    base_url = ""
    domain_name = ""
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = f"{Spider.project_name}/queue.txt"
        Spider.crawled_file = f"{Spider.project_name}/crawled.txt"
        self.boot()
        self.crawl_page("First spider", Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            Spider.add_links_to_queue(Spider.gather_link2(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
            print(f"{thread_name} now crawling {page_url}")
            print(f"Queue: {str(len(Spider.queue))}  |  Crawled: {str(len(Spider.crawled))}")

    @staticmethod
    def gather_link(page_url):
        html_string = ""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            request = urllib.request.Request(page_url, headers=headers)
            response = urllib.request.urlopen(request, timeout=10)
            # print("RESPONSE HEADER: " + response.getheader("Content-Type"))
            if response.getheader("Content-Type") == "text/html":
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(f"Error {e}, can not crawl page: {page_url}")
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

    @staticmethod
    def gather_link2(page_url):
        html_string = ""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            page = requests.get(page_url, headers=headers)
            soup = BeautifulSoup(page.content, "lxml")
            html_string = BeautifulSoup(soup.prettify(), "lxml")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(str(html_string))
        except Exception as e:
            print(f"Error {e}, can not crawl page: {page_url}")
            return set()
        return finder.page_links()
