import time
import matplotlib.pyplot as plt
import random

def create_matrix(order) -> list:
    mat = []
    for i in range(order):
        row = []
        for j in range(order):
            row.append(0)
        mat.append(row)
    return mat

def populate_matrix(mat, lim) -> list:
    for i in range(len(mat)):
        row = mat[i]
        for j in range(len(row)):
            row[j] = random.randint(0,lim)
    return mat

def matrix_multiply(mat1, mat2) -> list:
    res = create_matrix(len(mat1))
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            for k in range(len(mat1)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def mean_time(matmul_function, iterations: int, order: int) -> float:
    mean_time = 0.0
    for i in range(iterations):
        mat1 = populate_matrix(create_matrix(order), order * 10)
        mat2 = populate_matrix(create_matrix(order), order * 10)
        start = time.perf_counter()
        matmul_function(mat1,mat2)
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
    matmul_times = []
    n_vals = list(range(50,500,50))
    for n in n_vals:
        matmul_times.append(mean_time(matrix_multiply, 5, n))
    
    plot_algo(n_vals, ('Matrix Multiplication', matmul_times), 'matrixmul_analysis')


if __name__ == "__main__":
    main()