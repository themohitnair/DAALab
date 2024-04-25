import numpy as np
import matplotlib.pyplot as plt

def read_csv_data(csv_file):
    algorithm_data = {}

    with open(csv_file, 'r') as file:
        header = next(file).strip().split(',')
        algorithms = header[1:] 

        for algorithm in algorithms:
            algorithm_data[algorithm] = {'n_values': [], 'times': []}

        for line in file:
            parts = line.strip().split(',')
            n = int(parts[0])
            times = list(map(float, parts[1:])) 
            for i, algorithm in enumerate(algorithms):
                algorithm_data[algorithm]['n_values'].append(n)
                algorithm_data[algorithm]['times'].append(times[i])

    return algorithms, algorithm_data

def plot_timing_data(csv_file='timing_data.csv'):
    algorithms, algorithm_data = read_csv_data(csv_file)

    graph_title = input("Enter the title of the graph: ")
    x_label = input("Enter the label for the x-axis: ")
    y_label = input("Enter the label for the y-axis: ")

    plt.figure(figsize=(10, 6))

    for algorithm in algorithms:
        plt.plot(algorithm_data[algorithm]['n_values'], 
                 algorithm_data[algorithm]['times'], 
                 label=algorithm, 
                 marker='o', 
                 linestyle='-', 
                 alpha=0.8)

        for i, n in enumerate(algorithm_data[algorithm]['n_values']):
            plt.text(n, algorithm_data[algorithm]['times'][i], 
                     f'n={n}', ha='right', va='bottom', fontsize=8, alpha=0.8)

    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(graph_title, fontsize=14)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

plot_timing_data()
