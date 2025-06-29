#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT      1337
#define BACKLOG   5
#define BUF_SIZE  64
#define FLAG_PATH "flag.txt"

static int log_fd;

static void get_timestamp(char *buf, size_t len) {
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);
    strftime(buf, len, "%Y-%m-%d %H:%M:%S", tm_info);
}

void win(int client_fd) {
    FILE *f = fopen(FLAG_PATH, "r");
    if (!f) {
        dprintf(client_fd, "Erro ao abrir a flag. Contacta um mentor!\n");
        return;
    }

    char flagbuf[256];
    if (fgets(flagbuf, sizeof(flagbuf), f)) {
        dprintf(client_fd, "🎉 Exploit bem-sucedido! Flag: %s\n", flagbuf);
    } else {
        dprintf(client_fd, "Flag vazia ou leitura falhou. Contacta um mentor!\n");
    }

    fclose(f);
}

void handle_client(int client_fd, struct sockaddr_in *peer_addr) {
    char buf[BUF_SIZE];
    int auth = 0;

    char ts[64];
    get_timestamp(ts, sizeof(ts));
    printf("[%s] Cliente conectado: %s:%d\n", ts, inet_ntoa(peer_addr->sin_addr), ntohs(peer_addr->sin_port));
    fflush(stdout);

    log_fd = dup(STDOUT_FILENO);

    dup2(client_fd, STDIN_FILENO);
    dup2(client_fd, STDOUT_FILENO);
    dup2(client_fd, STDERR_FILENO);

    printf("Sê bem-vindo! Diz-me algo: ");
    fflush(stdout);

    if (gets(buf) == NULL) {
        get_timestamp(ts, sizeof(ts));
        dprintf(log_fd, "[%s] Cliente desconectou-se precocemente: %s:%d\n", ts, inet_ntoa(peer_addr->sin_addr), ntohs(peer_addr->sin_port));

        fflush(stdout);
        close(log_fd);
        return;
    }

    get_timestamp(ts, sizeof(ts));
    dprintf(log_fd, "[%s] Input recebido de %s:%d => %s\n", ts, inet_ntoa(peer_addr->sin_addr), ntohs(peer_addr->sin_port), buf);

    if (auth) {
        win(client_fd);
    } else {
        printf("Sem permissão para aceder à flag.\n");
    }

    close(log_fd);
}

int main() {
    int sockfd, client_fd;
    struct sockaddr_in addr;
    socklen_t sin_len = sizeof(addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    int opt = 1;
    setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    addr.sin_family      = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port        = htons(PORT);

    if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    if (listen(sockfd, BACKLOG) < 0) {
        perror("listen");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    while (1) {
        client_fd = accept(sockfd, (struct sockaddr *)&addr, &sin_len);
        if (client_fd < 0) {
            perror("accept");
            continue;
        }

        if (!fork()) {
            close(sockfd);
            handle_client(client_fd, &addr);
            close(client_fd);
            exit(0);
        }

        close(client_fd);
    }

    close(sockfd);
    return 0;
}
