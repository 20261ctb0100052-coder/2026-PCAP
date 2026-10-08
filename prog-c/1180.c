/*
 * Disciplina: 2025-PCAP
 * Problema : beecrowd 1180 - Menor e Posicao
 * Autor    : Pedro Noimann
 * LIAC     : Le N e depois N inteiros num vetor. Imprime o menor valor e a
 *            posicao em que ele esta (a partir de zero).
 */
#include <stdio.h>

int posicao_do_menor(int v[], int n) {
    int i, pos = 0;

    for (i = 1; i < n; i++) {
        if (v[i] < v[pos]) {
            pos = i;
        }
    }

     return pos; //
}

int main() {
    int v[1000], n, i, pos;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    pos = posicao_do_menor(v, n);

    printf("Menor valor: %d\n", v[pos]);
    printf("Posicao: %d\n", pos);

    return 0;
}