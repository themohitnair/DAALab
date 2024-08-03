import time
import matplotlib.pyplot as plt
import random
from sum_array import array_sum

def generate_random_array(size: int) -> list[int]:
    return [random.randint(0, size) for i in range(size)]

def get_mean_time(func: callable, sizes: list[int] = list(range(500, 10500, 500)), iterations: int = 100) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        array = generate_random_array(size)
        for i in range(iterations):
            start = time.perf_counter()
            func(array)
            end = time.perf_counter()
            total_time += (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(500, 10500, 500))):
    plt.figure(figsize=(10,6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Array Sizes')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    mean_times = get_mean_time(array_sum)
    plot("Sum of Array Elements", mean_times)

if __name__ == "__main__":
    main()