import time
import matplotlib.pyplot as plt
import random

def unique_check(a: list) -> bool:
    length = len(a)
    for i in range(length-1):
        for j in range(i+1, length):
            if a[j] == a[i]:
                return False
    return True

def unique_populate(n: int, lim: int) -> list:
    arr = []
    for i in range(n):
        randgen = random.randint(0,lim)
        while randgen in arr:
            randgen = random.randint(0,lim)
        arr.append(randgen)
    return arr

def mean_time(unique_check_func, n: int, iterations: int, a: list) -> float:
    mean_time = 0.0
    for i in range(iterations):
        start = time.perf_counter()
        unique_check_func(a)
        end = time.perf_counter()
        mean_time += (end - start)
    return mean_time/iterations

def plot_algo(x_axis: list, data_algo: tuple[str, list], filename: str):
    fig, ax = plt.subplots(figsize=(12,8))

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
    ucheck_times = []
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        ucheck_times.append(mean_time(unique_check, n, 1000, unique_populate(n, n*10)))
    
    plot_algo(n_vals, ('Array Unique Checking', ucheck_times), 'uniquecheck_analysis')

if __name__ == "__main__":
    main()