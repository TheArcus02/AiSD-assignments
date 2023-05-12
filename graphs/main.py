import time
import matplotlib.pyplot as plt
from makeGraphs import generate_eulerian_graph, Graph


def main():
    MAX_VERTICES = 16
    STEP = 1
    DENSITY = 0.5

    # setTimeComplexity(MAX_VERTICES, STEP, DENSITY)
    ex2SetTimeComplexity(MAX_VERTICES, STEP, DENSITY)

    generatePlot()


def setTimeComplexity(max_len: int, step: int, density: float):
    lengths = range(3, max_len, step)
    times = []

    algorithms = [eulerPath, hamiltonCycle]
    graphs: list[Graph] = []

    for data_len in range(3, max_len, step):
        graph = generate_eulerian_graph(data_len, density)
        graphs.append(graph)

    for algorithm in algorithms:
        for graph in graphs:
            start = time.perf_counter()
            algorithm(graph)
            stop = time.perf_counter()

            times.append(stop - start)
        plt.plot(lengths, times, label=f'{algorithm.__name__}')
        times = []


def ex2SetTimeComplexity(max_len: int, step: int, density: float):
    lengths = range(3, max_len, step)
    times = []

    for data_len in range(3, max_len, step):
        graph = generate_eulerian_graph(data_len, density)
        start = time.perf_counter()
        hamiltonCycle(graph, all_cycles=True)
        stop = time.perf_counter()
        times.append(stop - start)

    plt.plot(lengths, times, label='All Hamilton Cycles')


def hamiltonCycle(graph: Graph, all_cycles=False):
    return graph.findHamiltonCycle(all_cycles)


def eulerPath(graph: Graph):
    return graph.findEulerianPath()


def generatePlot(log=False, ylabel="Execution Time (s)"):
    plt.style.use("dark_background")
    plt.xlabel("List Length")
    plt.ylabel(ylabel)
    if log:
        plt.yscale('log')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
