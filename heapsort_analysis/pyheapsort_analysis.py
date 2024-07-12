import time
import matplotlib.pyplot as plt

def heapify(arr: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: list):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def mean_time(arr: list, sort_func, index: int):
    total_time = 0.0
    for i in range(index):
        start_time = time.perf_counter()
        sort_func(arr[:])
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time / index

def populate_array_descending(n: int):
    arr = list(range(n, 0, -1))
    return arr

def plot_algo(x_axis: list, data_algo: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12, 8))

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
    heapsort_times = []
    n_vals = list(range(50, 1000, 50))

    for n in n_vals:
        iterations = 100
        arr = populate_array_descending(n)
        heapsort_times.append(mean_time(arr, heap_sort, iterations))

    plot_algo(n_vals, ('Heap Sort', heapsort_times), 'heapsort_analysis')

if __name__ == "__main__":
    main()