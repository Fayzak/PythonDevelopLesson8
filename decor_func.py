import time
import os
import psutil


def decoration(f):
    def wrapper(*args, **kwargs):
        proc_start = psutil.Process(os.getpid())
        start_memory = proc_start.memory_info().rss/10**6
        start = time.clock()
        print(f(*args, **kwargs))
        end = time.clock()
        proc_end = psutil.Process(os.getpid())
        end_memory = proc_end.memory_info().rss/10**6
        print("Время выполнения функции: ", end - start)
        print("Память, которую заняла функция: ", end_memory - start_memory)
    return wrapper


@decoration
def stage(a, b):
    return a**b*10**100


stage(2, 3)