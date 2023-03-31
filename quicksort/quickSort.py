import random
import sys

# Incease recursion limit
sys.setrecursionlimit(2500)


def quick_sort(arr: list[int], low: int, high: int, pivotType: str = 'last') -> None:
    if low < high:
        # pivot

        pivot = arr[high]

        if pivotType == "median":
            pivot = arr[high//2]
        elif pivotType == "random":
            pivot = arr[random.randint(low, high)]

        # partition
        pi = partition(arr, low, high, pivot)

        # sort left
        quick_sort(arr, low, pi - 1, pivotType)

        # sort right
        quick_sort(arr, pi + 1, high, pivotType)


def partition(arr: list[int], low: int, high: int, pivot: int) -> int:

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i]

    # swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
