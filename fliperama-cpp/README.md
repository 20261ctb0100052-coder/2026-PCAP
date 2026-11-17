# Fliperama em C++ (MeuApp v4.0)

## O que e
[duas linhas suas: o que o programa faz e de onde ele veio]
O programa é um fliperama onde dá para cadastrar jogadores, ver a lista e brincar de adivinhar números. Ele foi feito a partir de um projeto em C, mas agora foi passado para C++, usando vetores e arquivos para guardar os dados dos jogadores.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: [uma linha]
- jogadores.csv: [uma linha: o que cada coluna guarda]

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 70) | apelidos.push_back(novo) (l.87) |
| comparar apelidos | strcmp(...) == 0 (l. 53) | == (l. 54) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 59) | void cadastrar(... &apelidos, ...) (l. 81) |

## O que o C++ decidiu por mim
[duas linhas: uma coisa que em C voce escrevia e em C++ a linguagem faz]
Em C, eu precisava cuidar do tamanho dos vetores e usar comandos como strcpy e strcmp para trabalhar com textos. Já em C++, ficou mais fácil usando string e vector, que ajudam a guardar e comparar as informações.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git |B| fliperama.cpp, estrutura do programa e função main()|
| 2. Cadastro: vetores e referencia |B| fliperama.cpp, funções cadastrar() e buscar()|
| 3. Jogo e partidas |B| fliperama.cpp, função jogar_adivinhe()|
| 4. Persistencia |B| fliperama.cpp, funções salvar() e carregar()|
| 5. Documentacao e comparacao |B| README.md, documentação e comparação entre C e C++|