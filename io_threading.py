import concurrent.futures
import requests
import threading
import time

#from easyLogger import EasyLogger



# requests.Session() is not thread-safe: operating system is in control of when your task gets interrupted and another task starts, any data that is shared between the threads needs to be protected, or thread-safe. 
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"): #When get_session() is called, the session it looks up is specific to the particular thread on which it’s running. So each thread will create a single session the first time it calls get_session() and then will simply use that session on each subsequent call throughout its lifetime.
        thread_local.session = requests.Session() # each thread needs to create its own requests.Session() object. Because in requests ducumentation,  a separate Session for each thread.
    return thread_local.session


def download_site(url):
    session = get_session()  # add this line compared with asynchronous
    with session.get(url) as response:
        #len(response.content)
        #log.info("Read {} from {}".format(len(response.content), url))
         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)


def download_all_sites(sites,thread_num):
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
        executor.map(download_site, sites) # runs the passed-in function on each of the sites in the list. 


#if __name__ == "__main__":
def get_time_download_sites(thread_num):
    #log = EasyLogger(name="io_threading", log_file_name="./log/io_threading.log")
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites,thread_num)
    duration = time.time() - start_time
    #log.info("{} threads: Downloaded {} in {} seconds".format(thread_num,len(sites), duration))
    #print(f"Downloaded {len(sites)} in {duration} seconds")
    return duration

get_time_download_sites(thread_num=30)