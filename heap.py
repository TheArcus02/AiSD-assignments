def heap_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)

    for i in range(arr_len//2, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)

    return arr


def heapify(arr: list[int], n: int, i: int):

    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        # swap
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
