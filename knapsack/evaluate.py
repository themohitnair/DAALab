import time
import matplotlib.pyplot as plt
from knapsack import knapsack
import random

def generate_knapsack_problem(num_items, weight_range=(1, 100), profit_range=(1, 100)):
    weights = []
    profits = []
    total_weight = 0
    
    for _ in range(num_items):
        weight = random.randint(*weight_range)
        profit = random.randint(*profit_range)
        weights.append(weight)
        profits.append(profit)
        total_weight += weight

    capacity = int(total_weight * 0.5)
    
    return profits, weights, capacity

def get_mean_time(func: callable, sizes: list[int] = list(range(5, 105, 5)), iterations: int = 20) -> list[float]:
    mean_times = []
    for size in sizes:
        total_time = 0.0
        profits, weights, capacity = generate_knapsack_problem(size)
        for i in range(iterations):
            start = time.perf_counter()
            func(profits, weights, capacity)
            end = time.perf_counter()
            total_time = (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], sizes: list[int] = list(range(5, 105, 5))):
    plt.figure(figsize=(10, 6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Array Sizes')
    plt.ylabel('Average Time Taken')
    plt.plot(sizes, param_list, marker="o", color="red")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    knapsack_mean_times = get_mean_time(knapsack)
    plot("Knapsack Problem", knapsack_mean_times)

if __name__ == "__main__":
    main()