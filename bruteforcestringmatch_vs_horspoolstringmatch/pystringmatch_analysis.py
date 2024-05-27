import string
import random
import time
import matplotlib.pyplot as plt

def naive_string_match(string: str, pattern: str, table=None):
    m = len(pattern)
    n = len(string)
    for i in range(n - m + 1):
        j = 0
        while j < m and string[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


def shift_table(pattern: str):
    m = len(pattern)
    table = []
    for i in range(128):
        table.append(m)
    for j in range(m - 1):
        table[ord(pattern[j]) - ord('0')] = m - 1 - j
    return table

def horspool_string_match(string: str, pattern: str, table: list):
    m = len(pattern)
    n = len(string)
    i = m - 1
    for i in range(n):
        j = 0
        while j < m and string[i - j] == pattern[m - 1 - j]:
            j += 1
        if j == m:
            return i - m + 1
        else:
            j += table[ord(string[j]) - ord('0')]
    return -1

def generate_random_string(length, exclude_letters: str):
    alphabets = list(string.ascii_letters)
    
    for letter in exclude_letters:
        if letter in alphabets:
            alphabets.remove(letter)
    
    random_string = ''.join(random.choices(alphabets, k=length))
    return random_string

def mean_time(match_func, iterations: int, length: int):
    total_time = 0.0
    for i in range(iterations):        
        pattern = 'AEIOUaeiou'
        table = shift_table(pattern)
        string = generate_random_string(length, pattern)
        start_time = time.perf_counter()
        match_func(string, pattern, table)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        total_time += time_elapsed
    return total_time/iterations

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
    naive_match_time = []
    horspool_match_time = []
    
    n_vals = list(range(50,1000,50))
    for n in n_vals:
        iterations = n * 10
        naive_match_time.append(mean_time(naive_string_match, iterations, n))
        horspool_match_time.append(mean_time(horspool_string_match, iterations, n))

    plot_comparison(n_vals, ('Naive String Match', naive_match_time), ('Horspool String Match', horspool_match_time), 'naive_vs_horspool')

if __name__ == "__main__":
    main()