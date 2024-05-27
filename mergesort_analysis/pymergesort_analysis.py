import time
import matplotlib.pyplot as plt

def merge_sort(a: list, low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge(a, low, mid, high)

def merge(a: list, low: int, mid: int, high: int):
    temp = []
    i = low
    j = mid + 1
    k = 0

    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
        k += 1

    while i <= mid:
        temp.append(a[i])
        i += 1
        k += 1

    while j <= high:
        temp.append(a[j])
        j += 1
        k += 1

    for idx in range(len(temp)):
        a[low + idx] = temp[idx]

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
    mergesort_times = []
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        iterations = 100
        arr = populate_array_descending(n)
        mergesort_times.append(mean_time(arr, merge_sort, iterations))
    
    plot_algo(n_vals, ('Merge Sort', mergesort_times), 'mergesort_analysis')

if __name__ == "__main__":
    main()