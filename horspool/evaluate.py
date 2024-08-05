import random
from boyer_moore_horspool import horspool_search, shift_table
import time
import matplotlib.pyplot as plt

def generate_random_string_and_pattern(size: int) -> (str, str):
    string = []
    for i in range(size):
        string.append(str(random.randint(0, 128)))
    string = "".join(string)
    pattern = []
    for i in range(size // 3):
        pattern.append(str(random.randint(0, 128)))
    pattern = "".join(pattern)
    return pattern, string

def get_mean_time(search_func: callable, sizes: list[int] = list(range(500, 10500, 500)), iterations: int = 300) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        pattern, string = generate_random_string_and_pattern(size)
        for i in range(iterations):
            start = time.perf_counter()
            search_func(pattern, string)
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
    horspool_mean_times = get_mean_time(horspool_search)
    plot("Horspool String Search", horspool_mean_times)

if __name__ == "__main__":
    main()