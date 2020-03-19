from io_threading import get_time_download_sites

from easyLogger import EasyLogger

import matplotlib.pyplot as plt

## Since the extra overhead of creating and destroying the threads erases any time savings.
## Plot duration against number of threads to check it out. 

def thread_opt():
    time_list=[]
    log = EasyLogger(name="io_threading", log_file_name="./log/io_threading.log")
    for thread_num in range(1,1000):
        time=get_time_download_sites(thread_num=thread_num)
        log.info("{} threads: finish in {} seconds".format(thread_num,time))
        time_list.append(time)
        print(time_list)
    return time_list

def plot_line(y):
    plt.figure(figsize=(10,6))
    x=[i for i in range(len(time_list))]
    plt.plot(x,y)
    plt.title('time took against number of threads')
    plt.savefig('./pic/'+str(len(time_list))+'.png')
    plt.show()
    return 

time_list=thread_opt()
plot_line(y=time_list)