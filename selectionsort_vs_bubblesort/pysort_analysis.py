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


def main():
    arr = []
    bubble_sort_time = []
    selection_sort_time = []
    
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        index = 25
        arr = populate_array_descending(n)
        bubble_sort_time.append(mean_time(arr, bubble_sort, index))
        selection_sort_time.append(mean_time(arr, selection_sort, index))

    plot_comparison(n_vals, ('Bubble Sort', bubble_sort_time), ('Selection Sort', selection_sort_time), 'bsort_vs_ssort')    


if __name__ == "__main__":
    main()