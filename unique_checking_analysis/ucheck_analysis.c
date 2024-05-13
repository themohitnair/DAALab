#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<time.h>

bool is_unique(int* a, int n) {
    for(int i = 0; i < (n - 1); i++) {
        for(int j = i+1; j < n; j++) {
            if(a[i] == a[j]) {
                return false;
            }
        }
    }
    return true;
}

double calculate_uniquecheck_time(int n, int iterations, int* a) {
    clock_t start, end;
    double elapsed_time = 0;
    for (int i = 0; i < iterations; i++) {
        start = clock();                
        is_unique(a, n);
        end = clock();
        elapsed_time += ((double)(end - start))/CLOCKS_PER_SEC;
    }
    return elapsed_time/iterations;
}

bool is_in_array(int *array, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (array[i] == num) {
            return true;
        }
    }
    return false;
}

int* populate_unique_array(int size, int limit) {
    int index = 0;
    int* array = (int*)malloc(size * sizeof(int));
    
    if (array == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    srand(time(NULL));
    
    while (index < size) {
        int random_num = rand() % limit;
        
        if (!is_in_array(array, index, random_num)) {
            array[index] = random_num;
            index++;
        }
    }

    return array;
}

int main(void) {
    int n[10] = {10,20,50,100,200,500,1000,2000,5000,10000};
    double uniq_check_elapsed;
    for(int i = 0; i < 10; i++) {
        int* a = populate_unique_array(n[i], n[i]*10);
        uniq_check_elapsed = calculate_uniquecheck_time(n[i], 1000, a);
        printf("\nFor %d elements:\n",n[i]);
        printf("Time elapsed: %11.4e\n",uniq_check_elapsed);
    }
}
