/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2137 - A Biblioteca do Senhor Severino
 * Autor     : Pedro Noimann
 * LIAC      : Leia a quantidade de livros e seus códigos.
 * Ordene os códigos em ordem crescente e mostre todos
 * os códigos com 4 dígitos.
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    vector<string> livros;
    int n, i;
    string codigo;

    while (cin >> n) {
        livros.clear();

        for (i = 0; i < n; i++) {
            cin >> codigo;
            livros.push_back(codigo);
        }

        sort(livros.begin(), livros.end());

        for (i = 0; i < n; i++) {
            cout << livros[i] << endl;
        }
    }

    return 0;
}
