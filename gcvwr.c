#include <stdio.h>
 
int main(void) {
    int gross;
    int truck;
    int index;

    printf("Enter the first row of the array: ");
    scanf("%i %i %i",&gross,&truck,&index);

    int cur = 0;
    int sum = 0;
    printf("Enter the second row of the array: ");
    for(int i = 0; i < index; i++){
        scanf("%d",&cur);
        sum += cur;
        cur = 0;
    }

    int output = (gross - truck) * 0.9 - sum;
    printf("%i",output);
    return 0;
}