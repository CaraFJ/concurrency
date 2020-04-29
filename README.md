# compare concurrent methods

## example
- example is based on example given in https://realpython.com/python-concurrency/ , made modifications to help better understanding.

- `cpu_multiprocessing_process.py` is using multiprocessing.process instead of pool. This file only aims at showing how to apply process module.

### how to select number of processes in multiprocessing?
[a good answer](https://stackoverflow.com/questions/9355472/are-there-any-guidelines-to-follow-when-choosing-number-of-processes-with-multip)


> If all of your threads/processes are indeed CPU-bound, you should run as many processes as the CPU reports cores. Due to HyperThreading, each physical CPU cores may be able to present multiple virtual cores. Call multiprocessing.cpu_count to get the number of virtual cores.

> If only p of 1 of your threads is CPU-bound, you can adjust that number by multiplying by p. For example, if half your processes are CPU-bound (p = 0.5) and you have two CPUs with 4 cores each and 2x HyperThreading, you should start 0.5 * 2 * 4 * 2 = 8 processes.

> If you have too many processes, the synchronization overhead will increase. If your program is little to none synchronization overhead, this won't impact the overall runtime, but may make other programs appear slower than they are unless you set your processes to a lower priority. Excessive numbers of processes (say, 10000) are fine in theory if your OS has a good scheduler. In practice, virtually any synchronization will make the overhead unbearable.

> If it's CPU-heavy, the number of cores is a sane starting point. If it's IO-heavy, mulitple processes won't help performance anyway. If it's mostly CPU with occasional IO (e.g. PNG optimisation), you can run a few processes more than the number of cores.

#### how to find out if it is cpu-bound or IO-bound?
> If you're not sure whether your application is CPU-bound and/or perfectly scaling, simply observe system load with different thread counts. You want the system load to be slightly under 100%, or the more precise uptime to be the number of virtual cores.

### example background:
for each url, download the contents from it and get the size.

Notes: 
Using a Session object from requests can accelerate process!

It is possible to simply use get() from requests directly, but creating a Session object allows requests to do some fancy networking tricks and really speed things up.

### How to run
```
python io_synchronous_no_io.py
python io_synchronous_no_session.py
python io_synchronous_print.py
python io_synchronous.py
python io_threading.py # uncomment last line first
python thread_optimize.py
```


### Result
#### I/O-Bound
assume with session if not mentioned

synchronous:
- without io: 35.08285307884216 seconds / 34.32341909408569 seconds  (run 2 times)
- io without session: 72.58061599731445 seconds / 86.126944065094 seconds
- io with print: 35.89998483657837 seconds / 33.560221910476685 seconds
- io with log: 48.693845987319946 seconds / 37.30951499938965 seconds


threading:
- if pick right amount of threads, fastest could be <1 secound 
see picture generated in pic folder, which draws duration needed against number of threads.
it shows duration is steadily decreasing until number of threads reaches 48. After that, the duration is fluctuating a lot.

asychronous:
- 8.557939052581787 seconds / 61.32081389427185 seconds /9.753045082092285 seconds 

multiprocessing:
- 2.70198130607605 seconds / 13.731471300125122 seconds / 2.713169813156128 seconds

#### CPU-Bound
synchrounous:
- 7.4234230518341064 seconds

multiprocessing:
- 1.3691179752349854 seconds



