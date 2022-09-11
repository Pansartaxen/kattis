#include <stdio.h>
#include <stdlib.h>

int main(void){
    int * numbers;
    int size;
    scanf("%i\n", &size);
    numbers = (int*)malloc(size * sizeof(int));
    for(int i = 0; i < size; i++){
        scanf("%i", &numbers[i]);
    }

    for(int i = 0; i < size; i++){
        for(int j = i + 1; j < size; j++){
            if(numbers[i] > numbers[j]){
                int temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }

    for(int i = 0; i < size; i++){
        if(numbers[i] == numbers[i + 1] - 1 && numbers[i] == numbers[i + 2] - 2){
            int a = i + 1;
            int b = i;
            while(numbers[b] == (numbers[a] - 1)){
                ++a;
                ++b;
            } 
            printf("%i-%i ", numbers[i], numbers[a-1]);
            i = a - 1;
        }
        else{
            printf("%i ", numbers[i]);
        }
    }
    
    return 0;
}
