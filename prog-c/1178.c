/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1172 - Array
Replacente 1
* Autor      : Pedro Noimann
* Data       : 2026.10.06
* LIAC       : Leia um valor real e guarde em N[0]. Preencha as posições de 1 a 99 com a metade da posição anterior. Mostre as cem posições com quatro casas decimais.*/
#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4lf\n", i, n[i]);
    }

    return 0;
}