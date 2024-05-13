#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int factorial_recursive(int n) {
    if (n < 0) {
        return -1;
    }
    else if (n <= 1) {
        return n;
    }
    else {
        return n * factorial_recursive(n-1);
    }
}

int factorial_iterative(int n) {
    int factorial = 1;
    for(int i = 1; i <= n; i++) {
        factorial *= i;
    }
    return factorial;
}

double calculate_factorial_recursive_time(int n, int k) {
    double time_elapsed = 0;
    for(int i = 0; i < k; i++) {
        clock_t start, end;
        start = clock();
        factorial_recursive(n);
        end = clock();
        time_elapsed += ((double)(end-start))/CLOCKS_PER_SEC;
    }
    time_elapsed /= k;
    return time_elapsed;
}

double calculate_factorial_iterative_time(int n, int k) {
    double time_elapsed = 0;
    for(int i = 0; i < k; i++) {
        clock_t start, end;
        start = clock();
        factorial_iterative(n);
        end = clock();
        time_elapsed += ((double)(end-start))/CLOCKS_PER_SEC;
    }
    time_elapsed /= k;
    return time_elapsed;
}

int main(void) {
    int n[10] = {10,20,50,100,200,500,1000,2000,5000,10000};
    double time_elapsed_recursive_factorial, time_elapsed_iterative_factorial;
    for(int i = 0; i < 10; i++) {
        time_elapsed_recursive_factorial = calculate_factorial_recursive_time(n[i], 1000);
        time_elapsed_iterative_factorial = calculate_factorial_iterative_time(n[i], 1000);
        
        printf("\nFor n = %d:\n", n[i]);
        printf("Recursive Factorial: %11.4e\tIterative Factorial: %11.4e\n", time_elapsed_recursive_factorial, time_elapsed_iterative_factorial);
    }
}