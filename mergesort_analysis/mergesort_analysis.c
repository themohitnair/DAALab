#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void merge(int* a, int low, int mid, int high) {
    int i = low;
    int j = mid + 1;
    int k = 0;

    if(low > high) {
        return;
    }

    int* temp = (int*)malloc(((size_t)(high - low + 1) )* sizeof(int));
    if(temp == NULL) { 
        printf("Memory allocation failed");
        exit(1);
    }

    while((i <= mid) && (j <= high)) {
        if(a[i] <= a[j]) {
            temp[k++] = a[i++];
        }
        else {
            temp[k++] = a[j++];
        }
    }

    while(i <= mid) {
        temp[k++] = a[i++];
    }

    while(j <= high) {
        temp[k++] = a[j++];
    }

    for(int m = low; m <=high; m++) {
        a[m] = temp[m - low];
    }

    free(temp);
}

void merge_sort(int* a, int low, int high) {
    if(low < high) {
        int mid = (low + high)/2;
        merge_sort(a, low, mid);
        merge_sort(a, mid + 1, high);
        merge(a, low, mid, high);
    }
}


double calculate_mergesort(int iterations, int size, int *arr) {
    double time_elapsed_selsort = 0;
    for (int k = 0; k < iterations; k++) {
        clock_t start = clock();
        merge_sort(arr, 0, size - 1);
        clock_t end = clock();
        double interval = ((double)(end - start)) / CLOCKS_PER_SEC;
        time_elapsed_selsort += interval;
    }
    return time_elapsed_selsort / iterations;
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

        double time_elapsed_mergesort = calculate_mergesort(1000, n[i], arr);

        printf("\nFor n = %d elements:\n", n[i]);
        printf("Merge Sort: %11.4e\n", time_elapsed_mergesort);

        free(arr);
    }

}