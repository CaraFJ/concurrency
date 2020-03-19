# compare concurrent methods

## example
- example is based on example given in https://realpython.com/python-concurrency/ , made modifications to help better understanding.

### example background:
for each url, download the contents from it and get the size.

Notes: 
Using a Session object from requests can accelerate process!

It is possible to simply use get() from requests directly, but creating a Session object allows requests to do some fancy networking tricks and really speed things up.

### How to run
`python io_synchronous_no_io.py`
`python io_synchronous_no_session.py`
`python io_synchronous_print.py`
`python io_synchronous.py`
`python io_threading.py # uncomment last line first` 
`python thread_optimize.py`



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



