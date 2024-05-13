#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int fibonacci_recursive(int n) {
    if((n == 1) || (n == 0)) {
        return n;
    }
    else {
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2));
    }
}

int fibonacci_iterative(int n) {
    int n0 = 0;
    int n1 = 1;
    if((n == 1) || (n == 0)) {
        return n;
    }
    else {
        n -= 1;
        int num;
        while(n > 0) {
            num = n0 + n1;
            n0 = n1;
            n1 = num;
            n--;
        }
        return num;
    }
}

double calculate_fibonacci_recursive_time(int n, int k) {
    double elapsed_time = 0;
    clock_t start, end;
    for(int i = 0; i < k; i++) {
        start = clock();
        fibonacci_recursive(n);
        end = clock();
        elapsed_time += (((double)(end - start))/CLOCKS_PER_SEC);
    }
    return elapsed_time/k;
}

double calculate_fibonacci_iterative_time(int n, int k) {
    double elapsed_time = 0;
    clock_t start, end;
    for(int i = 0; i < k; i++) {
        start = clock();
        fibonacci_iterative(n);
        end = clock();
        elapsed_time += (((double)(end - start))/CLOCKS_PER_SEC);
    }
    return elapsed_time/k;
}

int main(void) {
    int n[10] = {5,10,15,20,25,30,35,40,45,50};
    double fibonacci_recursive_time, fibonacci_iterative_time;
    for(int i = 0; i < 10; i++) {
        fibonacci_recursive_time = calculate_fibonacci_recursive_time(n[i],10);
        fibonacci_iterative_time = calculate_fibonacci_iterative_time(n[i],10);

        printf("\nFor n = %d:\n", n[i]);
        printf("Recursive Fibonacci: %11.4e\tIterative Fibonacci: %11.4e\n", fibonacci_recursive_time, fibonacci_iterative_time);
    }
}