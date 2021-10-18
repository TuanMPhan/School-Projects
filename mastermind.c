#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(int argc, char *argv[] ){
    int n = 12;
    int i;
    if (argc >0){
        char *code = malloc(5);
        char *guess = calloc(5,sizeof(char));
        char *test = calloc(5,sizeof(char));
        
        strcpy(code, argv[1]);
    
    


    printf("%s\n", "Available Colors: (B)lue (G)reen (O)range (P)urple (R)ed (Y)ellow");
 
    while(n>0){
        int b = 0;
        int w = 0;
        strcpy(test,code);
        
        printf("\n%s%d\n","No. guesses left: " , n);
        
        printf("%s","Enter your guess: ");
        
        scanf("%s", guess);
        for (i=0; i< 4;i++){
            if (guess[i] == code[i]){
                b += 1;
                test[i] = 'F';
                guess[i] = 'E';
            }
        }
        for (i=0;i<4; i++){
            char *seen= strchr(test, guess[i]);
            if(seen!= NULL){
                w+=1;
                
                *seen = 'F';
            }
        }
        printf("%s%d%s%d\n","        Feedback: ", b, ", ", w);
        n--;
        
        if (b==4){
            printf("%s\n", "YOU WIN!");
            break;
        }
    }
    free(test);
    free(code);
    free(guess);
    if (n==0){
        printf("%s%s\n", "YOU LOSE! The code is ", argv[1]);
    }
    }
    return 0;

}
