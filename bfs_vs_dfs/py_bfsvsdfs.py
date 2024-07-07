import random
import time
import matplotlib.pyplot as plt
from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def generate_random_graph(num_nodes, edge_prob):
    graph = defaultdict(set)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_prob:
                graph[i].add(j)
                graph[j].add(i)
    return graph

def mean_time(search_func, iterations, num_nodes, edge_prob):
    total_time = 0.0
    for _ in range(iterations):
        graph = generate_random_graph(num_nodes, edge_prob)
        start_node = random.choice(list(graph.keys()))
        start_time = time.perf_counter()
        search_func(graph, start_node)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time / iterations

def plot_comparison(x_axis, data_algo1, data_algo2, filename):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(x_axis, data_algo1[1], marker='o', label=data_algo1[0])
    ax.plot(x_axis, data_algo2[1], marker='o', label=data_algo2[0])
    ax.set_facecolor('lightgreen')
    ax.set_title(f'{data_algo1[0]} vs {data_algo2[0]}', fontsize=24)
    ax.set_xlabel('Number of Nodes (n)', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend()
    plt.savefig(filename)
    plt.show()

def main():
    bfs_time = []
    dfs_time = []
    n_vals = list(range(20, 200, 20))
    edge_prob = 0.1
    for n in n_vals:
        iterations = n * 10
        bfs_time.append(mean_time(bfs, iterations, n, edge_prob))
        dfs_time.append(mean_time(dfs_stack, iterations, n, edge_prob))
    plot_comparison(n_vals, ('BFS', bfs_time), ('DFS (Stack)', dfs_time), 'bfs_vs_dfs_stack')

if __name__ == "__main__":
    main()