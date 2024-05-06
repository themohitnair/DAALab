#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int binarysearch(int *arr, int key, int n) {
    int low = 0;
    int high = n - 1;
    int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (key == arr[mid]) {
            return mid;
        } else if (key < arr[mid]) {
            high = mid - 1;
        } else if (key > arr[mid]) {
            low = mid + 1;
        }
    }
    return -1;
}

int linearsearch(int *arr, int key, int n) {
    for (int i = 0; i < n; i++) {
        if (key == arr[i]) {
            return i;
        }
    }
    return -1;
}

double calculate_linsearch(int iterations, int size, int *arr, int key) {
    double time_elapsed_linear = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        int result_linear = linearsearch(arr, key, size);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_linear += interval;
    }
    return time_elapsed_linear / iterations;
}

double calculate_binsearch(int iterations, int size, int *arr, int key) {
    double time_elapsed_binary = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        int result_binary = binarysearch(arr, key, size);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_binary += interval;
    }
    return time_elapsed_binary / iterations;
}

int main(void) {
    int n[10] = {10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000};
    for (int i = 0; i < 10; i++) {
        int key = n[i] + 20;
        int *arr = (int *)malloc(n[i] * sizeof(int));
        if (arr == NULL) {
            perror("Memory allocation failed");
            return EXIT_FAILURE;
        }

        for (int j = 0; j < n[i]; j++) {
            arr[j] = rand() % (n[i] + 1);
        }

        double time_elapsed_linear = calculate_linsearch(1000, n[i], arr, key);
        double time_elapsed_binary = calculate_binsearch(1000, n[i], arr, key);
        

        printf("\nFor n = %d elements:\n", n[i]);
        printf("Linear Search: %11.4e\tBinary Search: %11.4e\n", time_elapsed_linear, time_elapsed_binary);

        free(arr);
    }
}