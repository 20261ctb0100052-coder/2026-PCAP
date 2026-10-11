/*
 * Disciplina: 2025-PCAP
 * Problema : beecrowd 1067
 * Autor    : Pedro Noimann
 */

#include <stdio.h>

int main() {
    int X;

    scanf("%d", &X);

    for (int i = 1; i <= X; i += 2) {
        printf("%d\n", i);
    }

    return 0;
}