import matplotlib.pyplot as plt
import time

def recursive_factorial(n: int) -> int:
    if(n < 0):
        return 1
    elif(n <= 1):
        return n
    else:
        return (n * recursive_factorial(n-1))
    
def iterative_factorial(n: int) -> int:
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def mean_time(fact_function, iterations: int, input: int):
    mean_time = 0.0
    for i in range(iterations):
        start_time = time.perf_counter()
        fact_function(input)
        end_time = time.perf_counter()
        mean_time += (end_time - start_time)
    mean_time /= iterations
    return mean_time

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
    recursive_factorial_times = []
    iterative_factorial_times = []
    n_vals = list(range(50,1000,50))

    for n in n_vals:
        recursive_factorial_times.append(mean_time(recursive_factorial,1000,n))
        iterative_factorial_times.append(mean_time(iterative_factorial,1000,n))

    plot_comparison(n_vals, ('Recursive Factorial',recursive_factorial_times), ('Iterative Factorial',iterative_factorial_times), 'factorial_recursive_vs_iterative')

if __name__ == "__main__":
    main()