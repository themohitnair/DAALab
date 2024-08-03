import matplotlib.pyplot as plt
from search_func import linear_search, binary_search
import random

def gen_array_and_key_linear(size: int, case: str) -> (list[int], int):
    if case not in {'w', 'b', 'a'}:
        raise ValueError("Case value must be 'w', 'b' or 'a'")
    if case == 'w':
        return list(range(size)), size   
    if case == 'b':
        return list(range(size)), 0
    if case == 'a':
        return [random.randint(0, size) for i in range(size)], random.randint(0, size)

def gen_array_and_key_binary(size: int, case: str) -> (list[int], int):
    if case not in {'w', 'b', 'a'}:
        raise ValueError("Case value must be 'w', 'b' or 'a'")
    if case == 'w':
        return list(range(size)), size
    if case == 'b':
        mid = size // 2
        array = list(range(size))
        return array, array[mid]
    if case == 'a':
        return [random.randint(0, size) for i in range(size)], random.randint(0, size)       

def get_comparison_numbers(search_func: callable, generation_function: callable, sizes: list[int], case: str) -> list[int]:
    comparison_numbers = []
    for size in sizes:
        array, key = generation_function(size, case)
        comparison_number = search_func(array, key)
        comparison_numbers.append(comparison_number)
    return comparison_numbers

def plot(algo_name: str, sizes: list[int], param_list_w: list[int], param_list_b: list[int], param_list_a: list[int]):
    plt.figure(figsize=(10,6))
    plt.grid(visible=True)
    plt.title(algo_name)
    plt.xlabel('Array Sizes')
    plt.ylabel('Number of Comparisons')
    plt.plot(sizes, param_list_w, marker="o", label="worst case", color="red")
    plt.plot(sizes, param_list_b, marker="o", label="best case", color="green")
    plt.plot(sizes, param_list_a, marker="o", label="average case", color="blue")
    plt.legend()
    plt.savefig(f'{algo_name}.png', dpi = 300)
    plt.show()

def main():
    sizes = list(range(500, 10500, 500))
    comparison_nums_linsearch_worst = get_comparison_numbers(linear_search, gen_array_and_key_linear, sizes, case='w')
    comparison_nums_linsearch_best = get_comparison_numbers(linear_search, gen_array_and_key_linear, sizes, case='b')
    comparison_nums_linsearch_average = get_comparison_numbers(linear_search, gen_array_and_key_linear, sizes, case='a')

    comparison_nums_binsearch_worst = get_comparison_numbers(binary_search, gen_array_and_key_binary, sizes, case='w')
    comparison_nums_binsearch_best = get_comparison_numbers(binary_search, gen_array_and_key_binary, sizes, case='b')
    comparison_nums_binsearch_average = get_comparison_numbers(binary_search, gen_array_and_key_binary, sizes, case='a')

    plot("Linear Search", sizes, comparison_nums_linsearch_worst, comparison_nums_linsearch_best, comparison_nums_linsearch_average)
    plot("Binary Search", sizes, comparison_nums_binsearch_worst, comparison_nums_binsearch_best, comparison_nums_binsearch_average)

if __name__ == "__main__":
    main()