from to_bin import dec_to_bin
import matplotlib.pyplot as plt
import time

def get_mean_time(func: callable, inputs: list[int] = list(range(500, 10500, 500)), iterations: int = 100) -> list[float]:
    mean_times = []
    for input in inputs:
        total_time = 0.0
        for i in range(iterations):
            start = time.perf_counter()
            dec_to_bin(input)
            end = time.perf_counter()
            total_time += (end - start)
        mean_times.append(total_time / iterations)
    return mean_times

def plot(algo_name: str, param_list: list[float], inputs: list[int] = list(range(500, 10500, 500))):
    plt.figure(figsize=(10,6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Inputs')
    plt.ylabel('Average Time Taken')
    plt.plot(inputs, param_list, marker="o", color="blue")
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    avg_time_taken = get_mean_time(dec_to_bin)
    plot("Decimal to Binary (Iterative)", avg_time_taken)

if __name__ == "__main__":
    main()