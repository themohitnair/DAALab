import argparse
import pandas as pd
import matplotlib.pyplot as plt

def plot_timing_data(csv_file):
    # Load the data from CSV into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Extract columns for n, Linear Search Time, and Binary Search Time
    n_values = data['n']
    linear_search_times = data['Linear Search Time']
    binary_search_times = data['Binary Search Time']

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, linear_search_times, label='Linear Search Time', marker='o', linestyle='-', color='b')
    plt.plot(n_values, binary_search_times, label='Binary Search Time', marker='s', linestyle='--', color='r')

    # Annotate each data point with its corresponding n value
    for i, n in enumerate(n_values):
        plt.text(n, linear_search_times[i], f'n={n}', ha='right', va='bottom', fontsize=8, color='b')
        plt.text(n, binary_search_times[i], f'n={n}', ha='right', va='top', fontsize=8, color='r')

    # Add labels and title
    plt.xlabel('n (Number of Elements)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Comparison of Linear and Binary Search Times', fontsize=14)
    plt.xscale('log')  # Use logarithmic scale for x-axis (n values)
    plt.yscale('log')  # Use logarithmic scale for y-axis (time values)
    plt.grid(True)
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Plot timing data from a CSV file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing timing data')
    args = parser.parse_args()

    # Call plot function with specified CSV file path
    plot_timing_data(args.csv_file)
