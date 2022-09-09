#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
    char * a;
    a = (char*)malloc(1000 * sizeof(char));
    scanf("%s" , a);
    int a_found = 0;
    for(int i = 0; i < 1000; i++){
        int ascii_a = (int)a[i];
        if(ascii_a == 'a' && a_found == 0){
            a_found = 1;
            printf("a");
        }
        else if (a_found == 1){
            printf("%c", a[i]);
        }
    }
    return 0;
}
