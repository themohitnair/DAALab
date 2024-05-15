import matplotlib.pyplot as plt
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

def merge_sort(arr: list, low: int, high: int): 
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    len1 = mid - low + 1
    len2 = high - mid

    # Create temporary arrays for left and right halves
    left_arr = arr[low:mid + 1]
    right_arr = arr[mid + 1:high + 1]

    i = 0  # Index for left_arr
    j = 0  # Index for right_arr
    k = low  # Index for merged array

    # Merge the left and right arrays back into arr
    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy remaining elements of left_arr, if any
    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right_arr, if any
    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1



        
def mean_time(arr: list, sort_func, index: int):
    total_time = 0.0
    for i in range(index):
        start_time = time.perf_counter()
        sort_func(arr)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time/index

def populate_array_descending(n: int):
    arr = list(range(n,0,-1))
    return arr

def plot_comparison(x_axis: list, data_algo2: tuple[str, list], data_algo1: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12,8))

    ax.plot(x_axis, data_algo1[1], marker='o', label=data_algo1[0])

    ax.plot(x_axis, data_algo2[1], marker='o', label=data_algo2[0])

    ax.set_facecolor('lightgreen')
    ax.set_title(f'{data_algo1[0]} vs {data_algo2[0]}', fontsize=24)
    ax.set_xlabel('Input Size (n)', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)  
    ax.tick_params(axis='y', labelsize=12)

    ax.legend()
    plt.savefig(filename)

    plt.show()


a = [3,5,4,1,7,0,2]
merge_sort(a, 0, len(a)-1)
print(a)