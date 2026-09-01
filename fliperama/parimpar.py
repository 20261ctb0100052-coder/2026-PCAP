# ==================================================================
# Conceitos: Jogo com modulo, lista, funcao com retorno e operador %
# Base: Jogo da Aula 17 (Atividade 11)
# Autor: [Pedro Noimann]
# Data: 2026.08.11
# ==================================================================
from telas import titulo, linha
from modulos import ler_numero
from random import randint


def jogar_parimpar():
    titulo('PAR OU IMPAR')

    jogador = ler_numero('Digite um numero: ', 0, 10)
    escolha = input('Voce escolhe par ou impar? ').strip().lower()

    maquina = randint(0, 10)
    soma = jogador + maquina

    if soma % 2 == 0:
        tipo_resultado = 'par'
    else:
        tipo_resultado = 'impar'

    print('Sua escolha:', escolha)
    print('Computador jogou:', maquina)
    print('Soma dos numeros:', soma)
    print('O resultado e:', tipo_resultado)

    linha()

    if escolha == tipo_resultado:
        print('Voce ganhou!')
    else:
        print('Voce perdeu!')

