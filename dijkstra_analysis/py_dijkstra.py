import time
import random
import heapq
import matplotlib.pyplot as plt

def dijkstra_algorithm(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(priority_queue, (distance, v))
    
    return dist

def mean_time(num_nodes, edge_prob, iterations):
    total_time = 0.0
    for _ in range(iterations):
        graph = generate_random_graph(num_nodes, edge_prob)
        start_node = random.choice(range(num_nodes))
        start_time = time.perf_counter()
        dijkstra_algorithm(graph, start_node)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time / iterations

def plot_algo(x_axis, data_algo, filename):
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(x_axis, data_algo, marker='o', label='Dijkstra Algorithm')
    ax.set_facecolor('lightgreen')
    ax.set_title('Dijkstra Algorithm Analysis', fontsize=24)
    ax.set_xlabel('Number of Nodes', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend()
    plt.savefig(filename)
    plt.show()

def generate_random_graph(num_nodes, edge_prob):
    graph = [[] for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            if random.random() < edge_prob:
                weight = random.randint(1, 10)
                graph[u].append((v, weight))
                graph[v].append((u, weight))
    return graph

def main():
    dijkstra_times = []
    n_vals = list(range(10, 200, 20))
    edge_prob = 0.5
    iterations = 10
    for n in n_vals:
        dijkstra_times.append(mean_time(n, edge_prob, iterations))

    plot_algo(n_vals, dijkstra_times, 'dijkstra_analysis.png')

if __name__ == "__main__":
    main()