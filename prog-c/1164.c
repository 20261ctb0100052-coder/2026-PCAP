/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1172 - Array
Replacente 1
* Autor      : Pedro Noimann
* Data       : 2026.10.06
* LIAC       : Leia N casos de teste. Para cada inteiro X, diga se X é perfeito: um número é perfeito quando é igual à soma dos seus divisores menores que ele (6 = 1 + 2 + 3).*/
#include <stdio.h>

int eh_perfeito(int n) {
    int i, soma = 0;

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            soma = soma + i;
        }
    }

    return soma == n;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);

        if (eh_perfeito(x)) {
            printf("%d eh perfeito\n", x);
        } else {
            printf("%d nao eh perfeito\n", x);
        }
    }

    return 0;
}