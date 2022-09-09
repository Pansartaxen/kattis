// #include <stdio.h>
// #include <string.h>

// int main(void){
//     //printf("Enter a string: \n");
//     char a[4] = "B";
//     int a_found = 0;
//     int count = 0;
//     while (strcmp(a, "\0") != 0 || count < 1000)
//     {
//         scanf("%c" , &a);
//         count += 1;
//         if(strcmp(a, "a") == 0){
//             a_found = 1;
//             printf("a");
//         }
//         else if (a_found == 1){
//             printf("%s", a);
//         }
//     }
//     return 0;
// }

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
    printf("Enter a string: \n");
    char *a = malloc(1000 * sizeof(char));
    scanf("%c" , *a);
    int a_found = 0;
    int index = 0;
    for(int i = 0; i < 1000; i++)
    {
    if(strcmp(a[i], "a") == 0){
        a_found = 1;
        index = i;
        printf("a");
        i = strlen(a);
    }
    printf("A found at index %d" , index);
    for(int j = index; j < strlen(a); j++)
    {
        printf("%c", a[j]);
    }
    printf("\n");
    return 0;
    }
}