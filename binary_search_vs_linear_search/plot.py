import argparse
import pandas as pd
import matplotlib.pyplot as plt

def plot_timing_data(csv_file):
    data = pd.read_csv(csv_file)

    n_values = data['n']
    linear_search_times = data['Linear Search Time']
    binary_search_times = data['Binary Search Time']

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, linear_search_times, label='Linear Search Time', marker='o', linestyle='-', color='b')
    plt.plot(n_values, binary_search_times, label='Binary Search Time', marker='s', linestyle='--', color='r')

    for i, n in enumerate(n_values):
        plt.text(n, linear_search_times[i], f'n={n}', ha='right', va='bottom', fontsize=8, color='b')
        plt.text(n, binary_search_times[i], f'n={n}', ha='right', va='top', fontsize=8, color='r')

    plt.xlabel('n (Number of Elements)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Comparison of Linear and Binary Search Times', fontsize=14)
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Plot timing data from a CSV file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing timing data')
    args = parser.parse_args()

    plot_timing_data(args.csv_file)
