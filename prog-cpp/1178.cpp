/*
 * Disciplina: 2026-PCAP
 * Problema  : beecowd 1178 - 
 * Autor     : Pedro Noimann
 * LIAC      : Leia cem números reais num vector. Mostre, com a posição, os que são menores ou iguais a 10, com uma casa decimal.
 */
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

void preencher(vector<double> &n, double primeiro) {
    int i;

    n.push_back(primeiro);

    for (i = 1; i < 100; i++) {
        n.push_back(n[i - 1] / 2);
    }
}

void mostrar(vector<double> &n) {
    int i, qtd = n.size();

    cout << fixed << setprecision(4);

    for (i = 0; i < qtd; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }
}

int main() {
    vector<double> n;
    double primeiro;

    cin >> primeiro;

    preencher(n, primeiro);
    mostrar(n);

    return 0;
}
