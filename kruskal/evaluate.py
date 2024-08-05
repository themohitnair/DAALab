import random
from kruskal import kruskal
import time
import matplotlib.pyplot as plt
import numpy as np

def generate_adjacency_matrix(n: int, k: int, p: float, min_weight=1, max_weight=10):
    adj_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(1, k // 2 + 1):
            adj_matrix[i, (i + j) % n] = random.randint(min_weight, max_weight)
            adj_matrix[i, (i - j) % n] = random.randint(min_weight, max_weight)
    
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i, j] != 0:
                if random.random() < p:
                    new_j = random.choice(list(set(range(n)) - set([i, j])))
                    adj_matrix[i, j] = adj_matrix[j, i] = 0
                    adj_matrix[i, new_j] = adj_matrix[new_j, i] = random.randint(min_weight, max_weight)
    
    return adj_matrix

def get_mean_times(func, sizes=list(range(5, 105, 5)), iterations=200):
    mean_times = []
    for size in sizes:
        total_time = 0.0
        k = min(4, size - 1)
        p = 0.1
        for _ in range(iterations):
            mat = generate_adjacency_matrix(size, k, p)
            start = time.perf_counter()
            func(mat)
            end = time.perf_counter()
            total_time += (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(5, 105, 5))):
    plt.figure(figsize=(10, 6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Matrix Orders')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi=300)
    plt.show()

def main():
    mean_times = get_mean_times(kruskal)
    plot("Kruskal", mean_times)

if __name__ == "__main__":
    main()