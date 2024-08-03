import time
import matplotlib.pyplot as plt
from matrix_even import mat_even
import random

def generate_matrix(order: int) -> list[list[int]]:
    mat = [[0] * order for i in range(order)]
    for i in range(order):
        for j in range(order):
            mat[i][j] = random.randint(0, order * order)
    return mat

def get_mean_times(func: callable, sizes: list[int] = list(range(50, 1050, 50)), iterations = 100) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        mat = generate_matrix(size)
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
    plt.xlabel('Matrix Orders')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    mean_times = get_mean_times(mat_even)
    plot("Even element matrix probe", mean_times)

if __name__ == "__main__":
    main()