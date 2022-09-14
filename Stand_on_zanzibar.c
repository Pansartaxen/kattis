#include <stdio.h>
#include <stdlib.h>
int main(void){
    int input, prev, new, cases;
    scanf("%i\n", &cases);
    for(int i = 0; i < cases; i++){
        input = 1;
        new = 0;
        prev = 0;
        while(input != 0){
            scanf("%i", &input);
            if(input > prev * 2 && prev != 0){
                new += input - prev * 2;
            }
            prev = input;
            }
        printf("%i\n", new);
        }
    return 0;
}