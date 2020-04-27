import time
import os
import psutil


def simple_array():
    array = [x for x in range(0, 10**6) if x > 0 and type(x) == int]
    return array


def generation_array():
    for x in range(0, 10**6):
        yield x


def comparison_time():
    start = time.clock()
    simple_array()
    end = time.clock()
    time_result_simple = end - start
    print("Время генерации простого списка: ", time_result_simple)

    start = time.clock()
    generation_array()
    end = time.clock()
    time_result_generation = end - start
    print("Время генерации генерируемого списка: ", time_result_generation)

    print("Генерация на {} быстрее простого".format(time_result_simple - time_result_generation))


def comparison_gen():
    simple_proc_start = psutil.Process(os.getpid())
    simple_start_memory = simple_proc_start.memory_info().rss / 10 ** 6
    simple_array()
    simple_proc_end = psutil.Process(os.getpid())
    simple_end_memory = simple_proc_end.memory_info().rss / 10 ** 6
    memory_result_simple = simple_end_memory - simple_start_memory
    print("Память генерации простого списка: ", memory_result_simple)

    gen_proc_start = psutil.Process(os.getpid())
    gen_start_memory = gen_proc_start.memory_info().rss / 10 ** 6
    generation_array()
    gen_proc_end = psutil.Process(os.getpid())
    gen_end_memory = gen_proc_end.memory_info().rss / 10 ** 6
    memory_result_gen = gen_end_memory - gen_start_memory
    print("Память генерации генерируемого списка: ", memory_result_gen)

    print("Генерация на {} меньше занимает памяти, чем простой".format(memory_result_simple - memory_result_gen))


comparison_gen()
comparison_time()