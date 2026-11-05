/*
 * Disciplina: 2026-PCAP
 * Problema  : beecowd 1548 - 
 * Autor     : Pedro Noimann
 * LIAC      : Leia N casos de teste. Em cada um, M notas, na ordem em que os estudantes estão na fila. A fila é reordenada da maior nota para a menor; mostre quantos estudantes ficaram na mesma posição em que estavam.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int na_mesma_posicao(vector<int> fila) {
    vector<int> ordenada = fila;
    int i, iguais = 0, qtd = fila.size();

    sort(ordenada.begin(), ordenada.end(), greater<int>());

    for (i = 0; i < qtd; i++) {
        if (fila[i] == ordenada[i]) {
            iguais++;
        }
    }

    return iguais;
}

int main() {
    vector<int> fila;
    int n, m, nota, caso, i;

    cin >> n;

    for (caso = 0; caso < n; caso++) {
        fila.clear();

        cin >> m;

        for (i = 0; i < m; i++) {
            cin >> nota;
            fila.push_back(nota);
        }

        cout << na_mesma_posicao(fila) << endl;
    }

    return 0;
}
