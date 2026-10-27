# Fliperama em C (MeuApp v3.0)

## O que e
[duas linhas suas: o que o programa faz e de onde ele veio]

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c: [uma linha]
- jogadores.csv [uma linha: o que cada coluna guarda]

## Python x C: o que mudou
| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | jogadores.append(novo) (l.strcpy(apelidos[qtd], novo) (aprox. l. 48)) | strcpy(apelidos[qtd], novo) (l. 48) |
| comparar apelidos | == (l.strcmp(apelidos[i], procurado) == 0 (aprox. l. 33)) | strcmp(...) == 0 (l. 33) |
| abrir sem arquivo | exists(ARQUIVO) (l.if (arquivo == NULL) (aprox. l. 101)) | fopen == NULL (l. 101) |

## O que o C me obrigou a decidir
[duas linhas: uma coisa que o Python decidia sozinho e voce teve de escrever]

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git |Estrutura, compilação e Git | A | fliperama.c: bibliotecas, constantes, funções e main(). Compilação com gcc -Wall. O histórico do Git comprova o versionamento do projeto.|
| 2. |Cadastro: menu, funcoes e vetores Cadastro: menu, funções e vetores| A | fliperama.c: funções mostrar_menu(), cadastrar(), buscar() e listar(), com os vetores apelidos e partidas.|
| 3. Jogo e partidas | Jogo e partidas | A | fliperama.c: função jogar_adivinhe(), que gera um número aleatório, valida os palpites, conta as tentativas e registra uma partida para o jogador.|
| 4. Persistencia | Persistência | A |fliperama.c: funções salvar() e carregar(), que gravam e recuperam os dados dos jogadores no arquivo jogadores.csv |
| 5. Documentacao e comparacao | Documentação e comparação | A |README.md: descrição do projeto, instruções de compilação e execução, explicação dos arquivos e comparação entre Python e C.|