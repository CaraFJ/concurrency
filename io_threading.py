import concurrent.futures
import requests
import threading
import time

from easyLogger import EasyLogger

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()  # add this line compared with asynchronous
    with session.get(url) as response:
        log.info("Read {} from {}".format(len(response.content), url))
        # print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    log = EasyLogger(name="io_threading", log_file_name="./log/io_threading.log")
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    log.info("Downloaded {} in {} seconds".format(len(sites), duration))
    # print(f"Downloaded {len(sites)} in {duration} seconds")
