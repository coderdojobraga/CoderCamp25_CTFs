#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 64
#define FLAG_PATH "flag.txt"

void win() {
    FILE *f = fopen(FLAG_PATH, "r");
    if (!f) {
        printf("Erro ao abrir a flag. Contacta um mentor!\n");
        return;
    }

    char flagbuf[256];
    if (fgets(flagbuf, sizeof(flagbuf), f)) {
        printf("🎉 Exploit bem-sucedido! Flag: %s\n", flagbuf);
    } else {
        printf("Flag vazia ou leitura falhou. Contacta um mentor!\n");
    }

    fclose(f);
}

int main() {
    char buf[BUF_SIZE];
    int auth = 0;

    printf("Sê bem-vindo! Diz-me algo: ");

    gets(buf);

    if (auth) {
        win();
    } else {
        printf("Sem permissão para aceder à flag.\n");
    }

    return 0;
}
