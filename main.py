import random
import time
import matplotlib.pyplot as plt
from typing import Callable
from insertion import insertion_sort

def main():
    MAX_LEN = 1000
    STEP = MAX_LEN // 10

    plt.style.use("dark_background")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    
    setTimesComplexity(MAX_LEN, STEP, insertion_sort)

    plt.legend()
    plt.show()

def updatePlot(lengths, times, label):
    plt.plot(lengths, times, label=label)

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
        updatePlot(lengths, times, f'{data_type} data')
        lengths = []
        times = []

def getData(length: int, d_type: str) -> list[int]:

    if d_type == 'const':
        return [1 for _ in range(length)]
    
    data = [random.randint(0, 99) for _ in range(length)]
    
    if d_type == 'random':
        return data 
    elif d_type == 'ascending':
        return sorted(data)
    elif d_type == 'descending':
        return sorted(data, reverse=True)
    elif d_type == 'v':
        return sorted(data[:length//2]) + sorted(data[length//2:], reverse=True)


if __name__ == '__main__':
    main()