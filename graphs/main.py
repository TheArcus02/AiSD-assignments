from makeGraphs import generate_eulerian_graph


def main():

    N = 10
    g1 = generate_eulerian_graph(N, 0.3)
    # g2 = generate_eulerian_graph(N, 0.7)
    print(g1)
    # print(g2)
    path1 = g1.findEulerianPath()
    # path2 = g2.findEulerianPath()
    print(path1)

    # print(path2)


if __name__ == '__main__':
    main()
