import random
import time
import matplotlib.pyplot as plt
from linkedList import LinkedList, Node
from BinarySearchTree import Node as BSTNode, insert, findNode, deleteTree


def main():
    LENGTH = 10000
    STEP = LENGTH // 15
    # compare creating time
    # compare_creating(LENGTH, STEP)

    # compare searching time
    # compare_searching(LENGTH, STEP)

    # compare deleting time
    compare_deleting(LENGTH, STEP)

    generate_plot()


def compare_creating(max_len: int, step: int):
    lengths = []
    times = []
    algorithms = [create_bst, create_linked_list]
    for algorithm in algorithms:
        for data_lenght in range(0, max_len, step):
            data = get_random_data(data_lenght)

            start = time.perf_counter()
            algorithm(data)
            stop = time.perf_counter()

            times.append(stop - start)
            lengths.append(data_lenght)
        plt.plot(lengths, times, label=f'{algorithm.__name__}')
        lengths = []
        times = []


def compare_searching(max_len: int, step: int):
    lengths = []
    times = []

    random_data = get_random_data(max_len)
    bst = create_bst(random_data)
    linkedList = create_linked_list(random_data)

    algorithms = [search_linked_list, search_bst]
    data_structures = [linkedList, bst]

    for algorithm, data_structure in zip(algorithms, data_structures):
        for data_lenght in range(0, max_len, step):
            data = get_random_data(data_lenght)

            start = time.perf_counter()
            algorithm(data, data_structure)
            stop = time.perf_counter()

            times.append(stop - start)
            lengths.append(data_lenght)
        plt.plot(lengths, times, label=f'{algorithm.__name__}')
        lengths = []
        times = []


def compare_deleting(max_len: int, step: int):
    lengths = []
    times = []

    algorithms = [delete_linked_list, delete_bst]
    linkedLists = []
    binary_search_trees = []

    for data_lenght in range(0, max_len, step):
        data = get_random_data(data_lenght)
        linkedLists.append(create_linked_list(data))
        binary_search_trees.append(create_bst(data))
        lengths.append(data_lenght)

    for algorithm, data_structures in zip(algorithms, [linkedLists, binary_search_trees]):
        for data_structure in data_structures:
            start = time.perf_counter()
            algorithm(data_structure)
            stop = time.perf_counter()

            times.append(stop - start)
        plt.plot(lengths, times, label=f'{algorithm.__name__}')
        times = []


def create_bst(data: list[int]):
    bst = None
    for element in data:
        bst = insert(bst, element)
    return bst


def create_linked_list(data: list[int]):
    linked_list = LinkedList()
    for element in data:
        linked_list.add_sorted(Node(element))
    return linked_list


def search_linked_list(data: list[int], linked_list: LinkedList):
    for element in data:
        linked_list.find_element(element)


def search_bst(data: list[int], bst: BSTNode):
    for element in data:
        findNode(bst, element)


def delete_linked_list(linked_list: LinkedList):
    linked_list.delete_list()


def delete_bst(bst: BSTNode):
    deleteTree(bst)


def get_random_data(len: int) -> list[int]:
    return random.sample(range(len), len)


def generate_plot(log=False):
    plt.style.use("dark_background")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    if log:
        plt.yscale('log')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
