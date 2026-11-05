/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1179 - Preenchimento de Vetor IV
 * Autor     : Pedro Noimann
 * LIAC      : 
 */

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> par, impar;
    int numero, i;

    for (i = 0; i < 15; i++) {
        cin >> numero;

        if (numero % 2 == 0) {
            par.push_back(numero);
        } else {
            impar.push_back(numero);
        }

        if (par.size() == 5) {
            for (int j = 0; j < 5; j++) {
                cout << "par[" << j << "] = " << par[j] << endl;
            }
            par.clear();
        }

        if (impar.size() == 5) {
            for (int j = 0; j < 5; j++) {
                cout << "impar[" << j << "] = " << impar[j] << endl;
            }
            impar.clear();
        }
    }

    for (size_t i = 0; i < impar.size(); i++) {
        cout << "impar[" << i << "] = " << impar[i] << endl;
    }

    for (size_t i = 0; i < par.size(); i++) {
        cout << "par[" << i << "] = " << par[i] << endl;
    }

    return 0;
}
