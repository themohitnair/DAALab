#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int bindigitcounting_iterative(int n) {
    int count = 1;
    while(n > 1) {
        n /= 2;
        count++;
    }
    return count;
}

int bindigitcounting_recursive(int n) {
    if (n == 0) {
        return n;
    }
    else {
        return 1 + bindigitcounting_recursive(n/2);
    }
}

double calculate_bindigitcounting_recursive_time(int n, int k) {
    double mean_time = 0;
    for(int i = 0; i < k; i++) {
        clock_t start, end;
        start = clock();
        bindigitcounting_recursive(n);
        end = clock();
        mean_time += ((double)(end - start))/CLOCKS_PER_SEC;
    }
    return (mean_time/k);
}

double calculate_bindigitcounting_iterative_time(int n, int k) {
    double mean_time = 0;
    for(int i = 0; i < k; i++) {
        clock_t start, end;
        start = clock();
        bindigitcounting_iterative(n);
        end = clock();
        mean_time += ((double)(end - start))/CLOCKS_PER_SEC;
    }
    return (mean_time/k);
}

int main(void) {
    int n[10] = {10,20,50,100,200,500,1000,2000,5000,10000};
    double bindigitcounting_iterative_time, bindigitcounting_recursive_time;
    for(int i = 0; i < 10; i++) {
        bindigitcounting_recursive_time = calculate_bindigitcounting_recursive_time(n[i], 10000);
        bindigitcounting_iterative_time = calculate_bindigitcounting_iterative_time(n[i], 10000);
        
        printf("\nFor n = %d:\n", n[i]);
        printf("Recursive Binary Digit counting: %11.4e\tIterative Binary Digit counting: %11.4e\n", bindigitcounting_recursive_time, bindigitcounting_iterative_time);
    }
}