/*
 * Disciplina: 2026-PCAP
 * Problema  : beecowd 1002
 * Autor     : Pedro Noimann
 * LIAC      : Le o raio R (real). Calcula a area com pi = 3.14159 e imprime "A=area" com quatro casas decimais.
 */
 #include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    std::cin >> r;
    area = 3.14159 * r * r;
    std::cout << fixed << setprecision(4);
    std::cout << "A=" << area << endl;

    return 0;
}