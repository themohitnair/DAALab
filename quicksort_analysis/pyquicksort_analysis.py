import time
import matplotlib.pyplot as plt

def partition(a: list, low: int, high: int) -> int:
    i = low - 1
    j = high + 1
    pivot = a[low]

    while(True):
        while(True):
            i += 1
            if not (a[i] < pivot):
                break

        while(True):
            j -= 1
            if not (a[j] > pivot):
                break

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]

def quick_sort(a: list, low: int, high: int):
    if low < high:
        pi = partition(a, low, high)
        quick_sort(a, low, pi)
        quick_sort(a, pi + 1, high)

def mean_time(arr: list, sort_func, index: int):
    total_time = 0.0
    for i in range(index):
        start_time = time.perf_counter()
        sort_func(arr, 0, len(arr) - 1)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time/index

def populate_array_descending(n: int):
    arr = list(range(n,0,-1))
    return arr

def plot_algo(x_axis: list, data_algo: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12,8))

    ax.plot(x_axis, data_algo[1], marker='o', label=data_algo[0])
    ax.set_facecolor('lightgreen')
    ax.set_title(f'{data_algo[0]} Analysis', fontsize=24)
    ax.set_xlabel('Input Size (n)', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)  
    ax.tick_params(axis='y', labelsize=12)

    ax.legend()
    plt.savefig(filename)

    plt.show()

def main():
    quicksort_times = []
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        iterations = 100
        arr = populate_array_descending(n)
        quicksort_times.append(mean_time(arr, quick_sort, iterations))
    
    plot_algo(n_vals, ('Quick Sort', quicksort_times), 'quicksort_analysis')

if __name__ == "__main__":
    main()