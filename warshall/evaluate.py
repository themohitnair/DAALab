import time
import matplotlib.pyplot as plt
from warshall import warshall
import random

def generate_random_adj_matrix(size: int) -> list[list[int]]:
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def get_mean_times(func: callable, sizes: list[int] = list(range(5, 105, 5)), iterations = 100) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        mat = generate_random_adj_matrix(size)
        for i in range(iterations):
            start = time.perf_counter()
            func(mat)
            end = time.perf_counter()
            total_time += (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(500, 10500, 500))):
    plt.figure(figsize=(10, 6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Number of Nodes')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    mean_times = get_mean_times(warshall)
    plot("Warshall Algorithm", mean_times)

if __name__ == "__main__":
    main()