#include <stdio.h>
#include <string.h>

int main(void){
    //printf("Enter a string: \n");
    char a[4] = "B";
    int a_found = 0;
    int count = 0;
    while (strcmp(a, "\0") != 0 || count < 1000)
    {
        scanf("%c" , &a);
        count += 1;
        if(strcmp(a, "a") == 0){
            a_found = 1;
            printf("a");
        }
        else if (a_found == 1){
            printf("%s", a);
        }
    }
    return 0;
}