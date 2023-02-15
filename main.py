import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from multiprocessing import cpu_count
import time

start_time = time.time()

PROJECT_NAME = "mediaexpert"
HOMEPAGE = "https://www.mediaexpert.pl/telewizory-i-rtv"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = f"{PROJECT_NAME}/queue.txt"
CRAWLED_FILE = f"{PROJECT_NAME}/crawled.txt"
NUMBER_OD_THREADS = cpu_count()
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OD_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        try:
            Spider.crawl_page(threading.current_thread().name, url)
            queue.task_done()
        except Exception as e:
            print(f"Error {str(e)}, for: {threading.current_thread().name} with {url}")


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(f"{str(len(queued_links))} links in the queue")
        create_jobs()


# Start
create_workers()
crawl()

print(f"Execution time is: {round(time.time() - start_time, 2)} seconds")
