/*
 * Disciplina: 2026-PCAP
 * Problema  : beecowd 1011 - 
 * Autor     : Pedro Noimann
 * LIAC      : Leia o raio R (inteiro) e mostre o volume da esfera, que é (4/3) vezes pi vezes R ao cubo, com pi igual a 3.14159, no formato "VOLUME = volume", com três casas decimais.
 */
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}