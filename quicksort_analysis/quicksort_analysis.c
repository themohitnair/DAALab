#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<time.h>

void swap(int *a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int hoare_partition(int* arr, int low, int high) {
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;

    while(true) {
        do {
            i++;
        } while(arr[i] < pivot);

        do {
            j--;
        } while(arr[j] > pivot);

        if(i >= j) {
            return j;
        }

        swap(&arr[i], &arr[j]);
    }
}

void quick_sort(int* arr, int low, int high) {
    if(low < high) {
        int pi = hoare_partition(arr, low, high);

        quick_sort(arr, low, pi);
        quick_sort(arr, pi + 1, high);
    }
}

double calculate_quicksort(int iterations, int size, int *arr) {
    double time_elapsed_quicksort = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        quick_sort(arr, 0, size - 1);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_quicksort += interval;
    }
    return time_elapsed_quicksort / iterations;
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
            if (j == 0) {
                arr[j] = rand() % (n[i] + 1);
            } else {
                int gen = rand() % (n[i] + 1);
                if (gen <= arr[j-1]) {
                    arr[j] = gen;
                }
            }
        }

        double time_elapsed_quicksort = calculate_quicksort(100000, n[i], arr);

        printf("\nFor n = %d elements:\n", n[i]);
        printf("Quick Sort: %11.4e\n", time_elapsed_quicksort);

        free(arr);
    }

}