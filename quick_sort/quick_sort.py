def sort(arr: list[int], low: int, high: int):
    if low < high:
        pi = hoare_partition(arr, low, high)

        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)

def hoare_partition(arr: list[int], low: int, high: int):
    pivot = arr[(low + high) // 2]
    n = len(arr)
    i = -1
    j = n

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr: list[int]) -> list[int]:
    sort(arr, 0, len(arr) - 1)
    return arr

print(quick_sort([5,4,3,2,1]))