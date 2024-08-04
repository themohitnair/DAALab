def merge_sort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2

        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        return merge(arr, l, r)

def merge(arr: list[int], l: list[int], r: list[int]):
    i = j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[i]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        k += 1
        i += 1

    while j < len(r):
        arr[k] = r[j]
        k += 1
        j += 1

    return arr