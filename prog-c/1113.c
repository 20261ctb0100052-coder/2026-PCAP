/*
 * Disciplina: 2025-PCAP
 * Problema : beecrowd 1113
 * Autor    : Pedro Noimann
 */

#include <stdio.h>

int main() {
    int X, Y;

    while (1) {
        scanf("%d %d", &X, &Y);

        if (X == Y) {
            break;
        }

        if (X < Y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
    }

    return 0;
}