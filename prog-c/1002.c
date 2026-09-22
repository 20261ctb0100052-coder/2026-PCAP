/*
Problema 1002 BeeCrowd
2026.09.22
Pedro Noimann
*/

#include <stdio.h>

int main() {
    double raio = 0.0, area = 0.0;

    const double PI = 3.14159;

    printf("Digite o valor do raio: ");

    scanf("%lf", &raio);
 
    area = PI * (raio * raio);

    printf("A=%.4lf\n", area);

    return 0;
}