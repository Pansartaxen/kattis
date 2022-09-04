#include <stdio.h>
#include<string.h>
/*#include <stdout.h>
#include <stdin.h>*/
 
int main(void) {
    char gross = 0;
    char truck = 0;
    int index = 0;
    char first_row[14] = {0};
    scanf("%c",&first_row[14]);
    for(int i = 0; i < sizeof(first_row); i++){
    if(&first_row[i] != " "){
        index++;
    }
    else if(&first_row[i] == "\n"){
        break;
    }
    else{
        gross *= 10;
        gross += first_row[i];
    }
}


    char second_row[400] = {0};
    char count = 0;
    char cur = 0;
    scanf("%c",&second_row[400]);
    for(int i = 0; i < sizeof(second_row); i++){
        if(&second_row[i] != (char *)' '){
            count += cur;
            cur = 0;
        }
        else if (&second_row[i] >= (char *)0 && &second_row[i] <= (char *)9)
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