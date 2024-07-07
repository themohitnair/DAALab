import random
import time
import matplotlib.pyplot as plt

def floyd_warshall(graph):
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]
    for u in range(len(graph)):
        dist[u][u] = 0
        for v, weight in graph[u]:
            dist[u][v] = weight

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def generate_random_graph(num_nodes, edge_prob, max_weight=10):
    graph = [[] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_prob:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
    return graph

def mean_time(graph_gen_func, num_nodes, edge_prob, algo_func, iterations):
    total_time = 0.0
    for _ in range(iterations):
        graph = graph_gen_func(num_nodes, edge_prob)
        start_time = time.perf_counter()
        algo_func(graph)
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
    floyd_warshall_times = []
    n_vals = list(range(2, 200, 20))
    edge_prob = 0.5
    for n in n_vals:
        iterations = 10
        floyd_warshall_times.append(mean_time(generate_random_graph, n, edge_prob, floyd_warshall, iterations))

    plot_algo(n_vals, ('Floyd-Warshall Algorithm', floyd_warshall_times), 'floyd_warshall_analysis')

if __name__ == "__main__":
    main()
