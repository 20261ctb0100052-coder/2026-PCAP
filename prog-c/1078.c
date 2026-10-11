/*
 * Disciplina: 2025-PCAP
 * Problema : beecrowd 1078
 * Autor    : Pedro Noimann
 */
#include <stdio.h>

int main() {
    int N;

    scanf("%d", &N);

    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", i, N, i * N);
    }

    return 0;
}