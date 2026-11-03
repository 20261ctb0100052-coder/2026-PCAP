/*
 * Disciplina: 2026-PCAP
 * Problema  : beecowd 1001 - Extremamente Basico
 * Autor     : Pedro Noimann
 * LIAC      : Le dois inteiros A e B, um por linha. Imprime a soma no
 *             formato "X = soma", com espacos em volta do sinal de igual.
 */
 #include <iostream>
using namespace std;

 int main() {
    int a, b;

    std::cin >> a >> b;
    std::cout << "X = " << a + b << endl;

    return 0;
 }