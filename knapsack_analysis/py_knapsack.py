import random
import time
import matplotlib.pyplot as plt

def knapsack(weights, values, W):
    n = len(values)
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

def generate_knapsack_problem(n, max_weight):
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]
    W = random.randint(max_weight, max_weight * n // 2)
    return weights, values, W

def mean_time(num_items, max_weight, algo_func, iterations):
    total_time = 0.0
    for _ in range(iterations):
        weights, values, W = generate_knapsack_problem(num_items, max_weight)
        start_time = time.perf_counter()
        algo_func(weights, values, W)
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
    knapsack_times = []
    n_vals = list(range(10, 200, 20))
    max_weight = 50
    for n in n_vals:
        iterations = 10
        knapsack_times.append(mean_time(n, max_weight, knapsack, iterations))

    plot_algo(n_vals, ('Knapsack Algorithm', knapsack_times), 'knapsack_analysis')

if __name__ == "__main__":
    main()