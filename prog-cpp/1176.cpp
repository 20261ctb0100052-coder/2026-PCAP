/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1176 - Fibonacci em Vetor
 * Autor     : Pedro Noimann
 * LIAC      : Leia T casos de teste. Para cada caso, leia um
 * número N e mostre o valor de Fibonacci na posição N.
 */
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<unsigned long long> fib(61);
    int t, n, i;

    fib[0] = 0;
    fib[1] = 1;

    for (i = 2; i <= 60; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    cin >> t;

    for (i = 0; i < t; i++) {
        cin >> n;

        cout << "Fib(" << n << ") = " << fib[n] << endl;
    }

    return 0;
}
