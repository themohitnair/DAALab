def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[i], a[min] = a[min], a[i]
    return a