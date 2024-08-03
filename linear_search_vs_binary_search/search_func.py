def linear_search(a: list[int], key: int) -> (int, int):
    comp = 0
    for i in range(len(a)):
        comp += 1
        if a[i] == key:
            return comp
    return comp

def binary_search(a: list[int], key: int) -> (int, int):
    comp = 0
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        comp += 1
        if key == a[mid]:
            return comp
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return comp