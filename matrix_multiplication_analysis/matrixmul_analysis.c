#include<stdio.h>
#include<time.h>
#include<stdlib.h>

double** create_matrix(int n) {
    double** mat = (double**)malloc(n*sizeof(double*));
    for(int i = 0; i < n; i++) {
        mat[i] = (double*)malloc(n*sizeof(double));
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            mat[i][j] = 0;
        }
    }
    return mat;
}

double** populate_matrix(double** mat, int n, int limit) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            mat[i][j] = rand() % limit;
        }
    }
    return mat;
}

double** multiply_matrices(double** mat1, double** mat2, int order) {
    double** res = create_matrix(order);
    for(int i = 0;  i < order; i++) {
        for(int j = 0; j < order; j++) {
            for(int k = 0; k < order; k++) {
                res[i][j] += (mat1[i][k] * mat2[k][j]);
            }
        }
    }
    return res;
}

void free_matrix(double** mat, int n) {
    for(int i = 0; i < n; i++) {
        free(mat[i]);
    }
    free(mat);
}

double calculate_matmul_time(int order, int iterations) {
    clock_t start, end;
    double elapsed_time = 0;
    for(int i = 0; i < iterations; i++) {
        double** mat1 = create_matrix(order);
        double** mat2 = create_matrix(order);
        populate_matrix(mat1,order,order);
        populate_matrix(mat2,order,order);
        start = clock();
        multiply_matrices(mat1, mat2, order);
        end = clock();
        elapsed_time += ((double)(end - start))/CLOCKS_PER_SEC;
    }
    return elapsed_time/iterations;
}

int main(void) {
    int n[10] = {10,20,50,100,200,500};
    double elapsed_matmul_time;
    for(int i = 0; i < 6; i++) {
        elapsed_matmul_time = calculate_matmul_time(n[i], 100);
        printf("\nFor %d elements:\n",n[i]);
        printf("Time elapsed: %11.4e\n",elapsed_matmul_time);
    }
}