import argparse
import pandas as pd
import matplotlib.pyplot as plt

def plot_timing_data(csv_file):
    data = pd.read_csv(csv_file)

    n_values = data['n']
    selection_sort_times = data['Selection Sort Time']
    bubble_sort_times = data['Bubble Sort Time']

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, selection_sort_times, label='Selection Sort Time', marker='o', linestyle='-', color='b')
    plt.plot(n_values, bubble_sort_times, label='Bubble Sort Time', marker='s', linestyle='--', color='r')

    for i, n in enumerate(n_values):
        plt.text(n, selection_sort_times[i], f'n={n}', ha='right', va='bottom', fontsize=8, color='b')
        plt.text(n, bubble_sort_times[i], f'n={n}', ha='right', va='top', fontsize=8, color='r')

    plt.xlabel('n (Number of Elements)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Comparison of Selection and Bubble Sort Times', fontsize=14)
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
