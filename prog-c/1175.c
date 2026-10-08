/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1172 - Array
Replacente 1
* Autor      : Pedro Noimann
* Data       : 2026.10.06
* LIAC       : Leia vinte inteiros num vetor N. Mostre o vetor com a ordem invertida: o último lido aparece na posição 0, o primeiro lido na posição 19.*/
#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i =0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[ 19 - i]);
    }

    return 0;
}