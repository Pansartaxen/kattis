#include <stdio.h>

int main(void){
    int a = 0;
    int ones, tens;
    //printf("Enter two numbers: \n");
    scanf("%i\n", &a);
    ones = a % 10;
    tens = (a / 10) % 10;
    printf("%i%i\n", ones, tens);
    return 0;
}