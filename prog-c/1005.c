/*
Problema 1005 BeeCrowd
2026.09.22
Pedro Noimann
*/

#include <stdio.h>

int main(){

    double A = 0, B = 0;

    scanf("%lf", &A);
    scanf("%lf", &B);

    double media = (A * 3.5 + B * 7.5) / 11;

    printf("MEDIA = %.5lf\n", media);

    return 0;
}
