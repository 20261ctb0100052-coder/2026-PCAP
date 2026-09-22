/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: [Pedro Noimann]
*/

// importa biblioteca padrão de entrada e saída
#include <stdio.h>

//defino a função principal o tipo int
int main(){
    //printf == Saía ==> Mostra na Tela
    //"entre aspas == texto"
    //comando se encerra com ;
    printf("Hello World!\n");

    // Receber 2 valores somar e mostrar o resultado
    int A=0, B=0;
    printf("Digite um valor: ");
    scanf("%d", &A);
    printf("Digite outro valor; ");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);

    // indica que chegou ao fim da função == retornado 0
    return 0;
}

/*
para copilar ==
gcc <nome do arquivo> -o nome-do=programa

para executar ==
./nome-do-programa
*/