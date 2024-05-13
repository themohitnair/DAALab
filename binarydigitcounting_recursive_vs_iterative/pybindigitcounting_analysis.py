import matplotlib.pyplot as plt
import time

def bindigitcounting_recursive(n: int) -> int:
    if n == 0:
        return n
    else:
        return (1 + n//2)

def bindigitcounting_iterative(n: int) -> int:
    count = 1
    while(n > 1):        
        n //= 2
        count += 1
    return count

def mean_time(bindigitcounting_function, iterations: int, input: int) -> int:
    mean_time = 0.0
    for i in range(iterations):
        start = time.perf_counter()
        bindigitcounting_function(input)
        end = time.perf_counter()
        mean_time += (end - start)
    return (mean_time/iterations)

def plot_comparison(x_axis: list, data_algo2: tuple[str, list], data_algo1: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12,8))

    ax.plot(x_axis, data_algo1[1], marker='o', label=data_algo1[0])

    ax.plot(x_axis, data_algo2[1], marker='o', label=data_algo2[0])

    ax.set_facecolor('lightgreen')
    ax.set_title(f'{data_algo1[0]} vs {data_algo2[0]}', fontsize=24)
    ax.set_xlabel('Input Size (n)', fontsize=18)
    ax.set_ylabel('Average Time (seconds)', fontsize=18)
    ax.tick_params(axis='x', labelsize=12)  
    ax.tick_params(axis='y', labelsize=12)

    ax.legend()
    plt.savefig(filename)

    plt.show()

def main():
    bindigitcounting_iterative_times = []
    bindigitcounting_recursive_times = []

    n_vals = list(range(50,1000,50))
    for n in n_vals:
        bindigitcounting_recursive_times.append(mean_time(bindigitcounting_recursive, 10000, n))
        bindigitcounting_iterative_times.append(mean_time(bindigitcounting_iterative, 10000, n))

    plot_comparison(n_vals, ('Recursive Binary Digit Counting', bindigitcounting_recursive_times), ('Iterative Binary Digit Counting', bindigitcounting_iterative_times), 'binarydigitcounting_recursive_vs_iterative')

if __name__ == "__main__":
    main()