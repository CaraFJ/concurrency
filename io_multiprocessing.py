import requests
import multiprocessing
import time

from easyLogger import EasyLogger

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    log = EasyLogger(name="io_multiprocessing", log_file_name="./log/io_multiprocessing.log")
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    log.info("Downloaded {} in {} seconds".format(len(sites), duration))
    # print(f"Downloaded {len(sites)} in {duration} seconds")