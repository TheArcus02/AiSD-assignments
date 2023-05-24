from knapsack_algorithms import knapSackDynamic, knapSackGreedy
import random
import time
import matplotlib.pyplot as plt


def main():
    MAX_WEIGHT = 100
    MAX_ITEMS = 30_000
    STEP = 1000

    '''
        Uncomment the function you want to run
        and generate graph from it
    '''
    constMaxWeight(MAX_WEIGHT, MAX_ITEMS, STEP)
    # constItems(MAX_WEIGHT, MAX_ITEMS, STEP)


def constMaxWeight(max_weight: int, max_items: int, step: int):

    times = []
    solves = [[], []]
    solve_quality = []
    lengths = range(1, max_items, step)
    algorithms = [knapSackDynamic, knapSackGreedy]

    figure, axis = plt.subplots(1, 2)
    axis[0].set_title(f'Execution Time (logaritmic scale)')
    axis[0].set_xlabel(f'List Length')
    axis[1].set_title(f'Solve Quality')
    axis[1].set_xlabel(f'List Length')

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

    # logaritmic scale for execution time
    axis[0].set_yscale('log')

    axis[0].legend()
    axis[1].legend()
    plt.show()


def constItems(max_weight: int, max_items: int, step: int):

    times = []
    solves = [[], []]
    solve_quality = []
    max_weights = range(1, max_weight, step)
    algorithms = [knapSackDynamic, knapSackGreedy]

    figure, axis = plt.subplots(1, 2)
    axis[0].set_title(f'Execution Time (logaritmic scale)')
    axis[0].set_xlabel(f'Max Weight')
    axis[1].set_title(f'Solve Quality')
    axis[1].set_xlabel(f'Max Weight')

    for idx, algorithm in enumerate(algorithms):
        for current_weight in max_weights:

            weights = [random.randint(1, current_weight)
                       for _ in range(max_items)]
            values = [random.randint(1, 1000) for _ in range(max_items)]

            start = time.perf_counter()
            result = algorithm(current_weight, weights, values, max_items)
            stop = time.perf_counter()

            solves[idx].append(result)
            times.append(stop - start)
        axis[0].plot(max_weights, times, label=f'{algorithm.__name__}')
        times = []

    for idx in range(len(solves[0])):
        solve_quality.append(solves[0][idx] - solves[1][idx] / solves[0][idx])
    axis[1].plot(max_weights, solve_quality, label='Solve Quality')

    # logaritmic scale for execution time
    axis[0].set_yscale('log')

    axis[0].legend()
    axis[1].legend()
    plt.show()


if __name__ == '__main__':
    main()
