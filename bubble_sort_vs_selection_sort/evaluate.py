from sort_funcs import bubble_sort, selection_sort
import matplotlib.pyplot as plt
import time

def generate_worst_case_arrays(size: int) -> list[int]:
    return list(range(size - 1, -1, -1))

def get_mean_time(sort_func: callable, sizes: list[int] = list(range(500, 10500, 500)), iterations: int = 25) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        array = generate_worst_case_arrays(size)
        for i in range(iterations):
            start = time.perf_counter()
            sort_func(array)
            end = time.perf_counter()
            total_time = (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(500, 10500, 500))):
    plt.figure(figsize=(10, 6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Array Sizes')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="red")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    bubblesort_mean_times = get_mean_time(bubble_sort)
    selectionsort_mean_times = get_mean_time(selection_sort)
    plot("Bubble Sort", bubblesort_mean_times)
    plot("Selection Sort", selectionsort_mean_times)

if __name__ == "__main__":
    main()