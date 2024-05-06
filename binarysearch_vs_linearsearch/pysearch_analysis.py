import matplotlib.pyplot as plt
import random
import time 


def linear_search(arr: list, key: int) -> int:
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr: list, key: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def mean_time(arr: list, key: int, search_func, index: int):
    total_time = 0.0
    for i in range(index):
        start_time = time.perf_counter()
        search_func(arr, key)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time/index

def populate_array(n: int):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,n))
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
    binary_search_time = []
    linear_search_time = []
    
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        index = n * 10
        arr = populate_array(n)
        key = n + 20
        linear_search_time.append(mean_time(arr, key, linear_search, index))
        binary_search_time.append(mean_time(arr, key, binary_search, index))

    plot_comparison(n_vals, ('Binary Search', binary_search_time), ('Linear Search', linear_search_time), 'bsearch_vs_lsearch')

    


if __name__ == "__main__":
    main()
    

