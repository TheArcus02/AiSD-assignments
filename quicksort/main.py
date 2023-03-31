import time
from matplotlib import pyplot as plt
from quickSort import quick_sort


def main():
    MAX_LEN = 4500
    STEP = MAX_LEN // 15

    data = getData(MAX_LEN)
    setTimeComplexity(MAX_LEN, STEP, data)

    plt.style.use("dark_background")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.legend()
    plt.show()


def getData(length: int) -> list[int]:
    return [x for x in range(length) if x % 2 != 0]  \
        + [x for x in range(length, 0, -1) if x % 2 == 0]


def setTimeComplexity(max_len: int, step: int, data: list[int]):
    lengths = []
    times = []

    pivotTypes = ['last', 'median', 'random']

    for pivotType in pivotTypes:
        for data_lenght in range(0, max_len, step):

            start = time.perf_counter()
            quick_sort(data, 0, data_lenght - 1, pivotType)
            stop = time.perf_counter()

            times.append(stop - start)
            lengths.append(data_lenght)

        # Updating plot
        plt.plot(lengths, times, label=f'{pivotType} pivot')
        lengths = []
        times = []


if __name__ == "__main__":
    main()
