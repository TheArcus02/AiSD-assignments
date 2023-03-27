def selection_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)

    for i in range(arr_len):
        min_index = i

        for j in range(i+1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

    return arr
