#include <stdio.h>
/*#include <stdout.h>
#include <stdin.h>*/
 
int main(void) {
    int gross = 0;
    int truck = 0;
    int index = 0;
    char first_row[14] = {0};
    gets( first_row );
    for(int i = 0; i < sizeof(first_row); i++){
    if(first_row[i] != ' '){
        index++;
    }
    else if (index == 0)
    {
        gross *= 10;
        gross += first_row[i];
    }
}


    char second_row[400] = {0};
    int count = 0;
    int cur = 0;
    gets(second_row);
    for(int i = 0; i < sizeof(second_row); i++){
        if(second_row[i] != ' '){
            count += cur;
            cur = 0;
        }
        else if (second_row[i] >= 0 && second_row[i] <= 9)
        /*Måste få in variabeln i jämförelsen utan att den läses bokstavligt*/
        {
            cur *= 10;
            cur += second_row[i];
        }
        else
        {
            break;
        }
        
    }
    return 0;
}