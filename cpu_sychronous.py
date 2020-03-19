import time
from easyLogger import EasyLogger

def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    log = EasyLogger(name="cpu_synchronous", log_file_name="./log/cpu_synchronous.log")
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    log.info("Duration {} seconds".format(duration))
    #print(f"Duration {duration} seconds")