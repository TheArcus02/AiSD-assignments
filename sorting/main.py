import random
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from insertion import insertion_sort
from selection import selection_sort
from heap import heap_sort
from merge import merge_sort


def main():
    # constants
    MAX_LEN = 5000
    STEP = MAX_LEN // 15

    # Set one of following sorting algorithms
    # insertion_sort, selection_sort, heap_sort, merge_sort
    # Used only for setTimesComplexity function
    ALGORITHM = merge_sort

    # Set one of following data types
    # ascending, descending, random, const, v
    # Used only for compareAlgorithms function
    DATA_TYPE = 'v'

    # Use one of the following functions to either compare times complexity
    # for particular sorting algorithm or compare different algorithms
    # Comment out the one you don't want to use

    # setTimesComplexity(MAX_LEN, STEP, ALGORITHM)

    compareAlgorithms(MAX_LEN, STEP, DATA_TYPE, [
                      insertion_sort, selection_sort, heap_sort, merge_sort])

    # plot configuration
    plt.style.use("dark_background")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.legend()
    plt.show()


def setTimesComplexity(max_len: int, step: int, sortFunc: Callable):

    data_types = ['ascending', 'descending', 'random', 'const', 'v']
    lengths = []
    times = []
    for data_type in data_types:
        for data_lenght in range(0, max_len, step):
            data = getData(data_lenght, data_type)

            start = time.perf_counter()
            sortFunc(data)
            stop = time.perf_counter()

            times.append(stop - start)
            lengths.append(data_lenght)

        # Updating plot
        plt.plot(lengths, times, label=f'{data_type} data')
        lengths = []
        times = []


def compareAlgorithms(max_len: int, step: int, dataType: str, algorithms: list[Callable]):
    lengths = []
    times = []

    for alogrithm in algorithms:
        for data_lenght in range(0, max_len, step):
            data = getData(data_lenght, dataType)

            start = time.perf_counter()
            alogrithm(data)
            stop = time.perf_counter()

            times.append(stop - start)
            lengths.append(data_lenght)

        # Updating plot
        plt.plot(lengths, times, label=f'{alogrithm.__name__}')
        lengths = []
        times = []


def getData(length: int, d_type: str) -> list[int]:

    if d_type == 'const':
        return [1 for _ in range(length)]

    data = [random.randint(0, length) for _ in range(length)]

    if d_type == 'random':
        return data
    elif d_type == 'ascending':
        return sorted(data)
    elif d_type == 'descending':
        return sorted(data, reverse=True)
    elif d_type == 'v':
        return [x for x in range(length, 0, -1) if x % 2 == 0]  \
            + [x for x in range(length) if x % 2 != 0]
    return data


if __name__ == '__main__':
    main()
