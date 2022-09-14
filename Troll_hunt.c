#include <stdio.h>
#include <stdlib.h>
int main(void){
    int bridges;
    int knights;
    int size;
    scanf("%i %i %i", &bridges, &knights, &size);
    if((bridges - 1) % (knights / size) == 0){
        printf("%i\n", (bridges - 1) / (knights / size));
    }
    else{
        printf("%i\n", ((bridges - 1) / (knights / size))+1);
    }
    return 0;
}