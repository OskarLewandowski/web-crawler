from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


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
            print(f"{thread_name} now crawling {page_url}")
            print(f"Queue: {str(len(Spider.queue))}\nCrawled: {str(len(Spider.crawled))}")
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
