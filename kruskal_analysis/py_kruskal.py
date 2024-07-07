import time
import random
import matplotlib.pyplot as plt

def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal_algorithm(graph, num_nodes):
    edges = []
    for u in range(num_nodes):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()
    
    parent = list(range(num_nodes))
    rank = [0] * num_nodes
    mst = []
    
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
    
    return mst

def mean_time(num_nodes, edge_prob, iterations):
    total_time = 0.0
    for _ in range(iterations):
        graph = generate_random_graph(num_nodes, edge_prob)
        start_time = time.perf_counter()
        kruskal_algorithm(graph, num_nodes)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time / iterations

def generate_random_graph(num_nodes, edge_prob):
    graph = [[] for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            if random.random() < edge_prob:
                weight = random.randint(1, 10)
                graph[u].append((v, weight))
                graph[v].append((u, weight))
    return graph

def plot_algo(x_axis, data_algo, filename):
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(x_axis, data_algo, marker='o', label='Kruskal Algorithm')
    ax.set_facecolor('lightgreen')
    ax.set_title('Kruskal Algorithm Analysis', fontsize=24)
    ax.set_xlabel('Number of Nodes', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend()
    plt.savefig(filename)
    plt.show()

def main():
    kruskal_times = []
    n_vals = list(range(10, 200, 20))
    edge_prob = 0.5
    iterations = 10
    for n in n_vals:
        kruskal_times.append(mean_time(n, edge_prob, iterations))

    plot_algo(n_vals, kruskal_times, 'kruskal_analysis.png')

if __name__ == "__main__":
    main()
