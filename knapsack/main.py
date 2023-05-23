from knapsack_algorithms import knapSackDynamic, knapSackGreedy
import random
import time
import matplotlib.pyplot as plt


def main():

    constMaxWeight(100, 1000, 100)
    generate_plot(log=False)


def constMaxWeight(max_weight: int, max_items: int, step: int):

    times = []
    solves = [[], []]
    solve_quality = []
    lengths = range(10, max_items, step)
    algorithms = [knapSackDynamic, knapSackGreedy]

    figure, axis = plt.subplots(1, 2)
    axis[0].set_title(f'Execution Time')
    axis[1].set_title(f'Solve Quality')

    for idx, algorithm in enumerate(algorithms):
        for data_length in lengths:
            weights = [random.randint(1, max_weight)
                       for _ in range(data_length)]
            values = [random.randint(1, 1000) for _ in range(data_length)]

            start = time.perf_counter()
            result = algorithm(max_weight, weights, values, data_length)
            stop = time.perf_counter()

            solves[idx].append(result)
            times.append(stop - start)
        axis[0].plot(lengths, times, label=f'{algorithm.__name__}')
        times = []

    for idx in range(len(solves[0])):
        solve_quality.append(solves[0][idx] - solves[1][idx] / solves[0][idx])
    axis[1].plot(lengths, solve_quality, label='Solve Quality')

    axis[0].legend()
    axis[1].legend()


def generate_plot(log=False):
    plt.style.use("dark_background")
    plt.xlabel("List Length")
    if log:
        plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    main()
