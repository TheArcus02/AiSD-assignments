import time
import matplotlib.pyplot as plt
from makeGraphs import generate_eulerian_graph, Graph


def main():
    MAX_VERTICES = 17
    STEP = 1
    DENSITY = 0.7

    setTimeComplexity(MAX_VERTICES, STEP, DENSITY)

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


def hamiltonCycle(graph: Graph):
    return graph.findHamiltonCycle(all_cycles=False)


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
