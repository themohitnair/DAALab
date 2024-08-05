import random
from breadth_first_search import bfs
import time
import matplotlib.pyplot as plt

def generate_adjacency_matrix(n: int, edge_probability: float) -> tuple[list[list[int]], int]:
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_probability:
                weight = random.randint(1, 10)
                matrix[i][j] = weight
                matrix[j][i] = weight
    
    source_node = random.randint(0, n - 1)
    
    return matrix, source_node

def get_mean_times(func, sizes=list(range(5, 105, 5)), iterations=200):
    mean_times = []
    for size in sizes:
        total_time = 0.0
        p = 0.1
        for _ in range(iterations):
            mat, src = generate_adjacency_matrix(size, p)
            start = time.perf_counter()
            func(mat, src)
            end = time.perf_counter()
            total_time += (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(5, 105, 5))):
    plt.figure(figsize=(10, 6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Number of nodes')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi=300)
    plt.show()

def main():
    mean_times = get_mean_times(bfs)
    plot("Breadth-first Search", mean_times)

if __name__ == "__main__":
    main()
