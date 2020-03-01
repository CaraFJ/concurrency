import requests
import time

from easyLogger import EasyLogger


def download_site(url, session):
    with session.get(url) as response:
        log.info("Read {} from {}".format(len(response.content), url))
        # print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    log = EasyLogger(name="io_synchronous", log_file_name="./log/io_synchronous.log")
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    log.info("Downloaded {} in {} seconds".format(len(sites), duration))
    # print(f"Downloaded {len(sites)} in {duration} seconds")
