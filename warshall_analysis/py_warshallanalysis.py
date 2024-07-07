import random
import time
import matplotlib.pyplot as plt

def warshall(graph):
    n = len(graph)
    reach = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            reach[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

def generate_random_adj_matrix(num_nodes, edge_prob):
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_prob:
                matrix[i][j] = 1
    return matrix

def mean_time(num_nodes, edge_prob, algo_func, iterations):
    total_time = 0.0
    for _ in range(iterations):
        matrix = generate_random_adj_matrix(num_nodes, edge_prob)
        start_time = time.perf_counter()
        algo_func(matrix)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time / iterations

def plot_algo(x_axis, data_algo, filename):
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
    warshall_times = []
    n_vals = list(range(10, 200, 20))
    edge_prob = 0.5
    for n in n_vals:
        iterations = 10
        warshall_times.append(mean_time(n, edge_prob, warshall, iterations))

    plot_algo(n_vals, ('Warshall Algorithm', warshall_times), 'warshall_analysis')

if __name__ == "__main__":
    main()