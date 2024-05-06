#include<time.h>
#include<stdlib.h>
#include<stdio.h>

void selectionsort(int* arr, int n) {
    for(int i = 0; i < (n-1); i++) {
        int min = i;
        for(int j = i+1; j < n; j++) {
            if(arr[j] < arr[min]) {
                min = j;
            }
        }
        if (min != i) {
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }
}

void bubblesort(int* arr, int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-1-i; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

double calculate_selsort(int iterations, int size, int *arr) {
    double time_elapsed_selsort = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        selectionsort(arr, size);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_selsort += interval;
    }
    return time_elapsed_selsort / iterations;
}

double calculate_bubsort(int iterations, int size, int *arr) {
    double time_elapsed_bubsort = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        bubblesort(arr, size);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_bubsort += interval;
    }
    return time_elapsed_bubsort / iterations;
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

        double time_elapsed_selsort = calculate_selsort(1000, n[i], arr);
        double time_elapsed_bubsort = calculate_bubsort(1000, n[i], arr);

        printf("\nFor n = %d elements:\n", n[i]);
        printf("Selection Sort: %11.4e\tBubble Sort: %11.4e\n", time_elapsed_selsort, time_elapsed_bubsort);

        free(arr);
    }

}