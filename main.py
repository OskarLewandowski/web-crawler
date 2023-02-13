import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = "toscrape"
HOMEPAGE = "https://books.toscrape.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = f"{PROJECT_NAME}/queue.txt"
CRAWLED_FILE = f"{PROJECT_NAME}/crawled.txt"
NUMBER_OD_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
