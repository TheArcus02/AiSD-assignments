from makeGraphs import generate_eulerian_graph, Graph


def main():

    N = 12

    g1 = generate_eulerian_graph(N, 0.3)
    print(g1)
    cycleExists = g1.findHamiltonCycle(all_cycles=True)


if __name__ == '__main__':
    main()


'''
[[0, 1, 0, 1, 0],
 [1, 0, 1, 1, 1],
 [0, 1, 0, 0, 1,],
 [1, 1, 0, 0, 1],
 [0, 1, 1, 1, 0], ]
'''
