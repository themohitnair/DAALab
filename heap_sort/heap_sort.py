def heapify(arr: list[int], n: int, i: int):
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[lar] < arr[l]:
        lar = l

    if r < n and arr[lar] < arr[r]:
        lar = r

    if lar != i:
        arr[lar], arr[i] = arr[i], arr[lar]
        heapify(arr, n, lar)

def heap_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr