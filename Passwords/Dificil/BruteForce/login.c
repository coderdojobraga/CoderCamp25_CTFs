#include <stdio.h>
#include <string.h>

/*
argc (argument count) – an integer that tells you how many arguments were passed to the program from the command line.
argv (argument vector) – an array of strings (char*[]), where each string is one of the arguments.
*/

int main(int argc, char *argv[]) {
    
    if (argc < 2 || argc > 2) {
        printf("# %s <password>\n", argv[0]); //argv[0] == "./login"
        return 1;
    }

    char senha[10] = "coderdojo";
    if (strcmp(argv[1], senha) == 0) printf("Flag: CD25{passwords-forcabruta}\n");
    else printf("A password %s está incorreta!\n", argv[1]);

    return 0;
}