import matplotlib.pyplot as plt
import time

def fibonacci_iterative(n: int) -> int:
    n0 = 0
    n1 = 1
    if (n == 0) or (n == 1):
        return n
    elif n > 1:
        while (n - 1) > 0:
            num = n1 + n0
            n0 = n1
            n1 = num
            n -= 1
        return num
            
def fibonacci_recursive(n: int) -> int:
    if (n == 0) or (n == 1):
        return n
    elif n > 1:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

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

def mean_time(fibonacci_function, iterations: int, input: int):
    mean_time = 0.0
    for i in range(iterations):
        start_time = time.perf_counter()
        fibonacci_function(input)
        end_time = time.perf_counter()
        mean_time += (end_time - start_time)
    mean_time /= iterations
    return mean_time

def main():
    recursive_fibonacci_times = []
    iterative_fibonacci_times = []
    n_vals = list(range(2,40,2))

    for n in n_vals:
        recursive_fibonacci_times.append(mean_time(fibonacci_recursive,5,n))
        iterative_fibonacci_times.append(mean_time(fibonacci_iterative,5,n))

    plot_comparison(n_vals, ('Recursive Fibonacci',recursive_fibonacci_times), ('Iterative Fibonacci',iterative_fibonacci_times), 'fibonacci_recursive_vs_iterative')

if __name__ == "__main__":
    main()