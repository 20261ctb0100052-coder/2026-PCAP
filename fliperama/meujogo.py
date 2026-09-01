
# ============================================================
# ARQUIVO    : meujogo.py (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 23 - O jogo autoral do meu fliperama
# Autor      : []
# Conceitos  : Reuso de modulo proprio, funcao sem retorno,
#              entrada validada, contagem de partidas
# ============================================================

from telas import titulo, linha
from modulos import ler_numero
from random import randint


def jogar_meujogo():
    '''
    Jogo de rolar dados e comparar o resultado do jogador
    com o resultado do computador.
    '''

    titulo("MEU JOGO")

    # -------- REGRAS DO JOGO --------

    print("Vamos rolar os dados!")

    input("Pressione ENTER para rolar o seu dado...")

    jogador = randint(1, 6)

    print("Voce rolou:", jogador)

    linha()

    input("Pressione ENTER para o computador rolar o dado...")

    computador = randint(1, 6)

    print("Computador rolou:", computador)

    linha()

    if jogador > computador:
        print("Voce ganhou!")

    elif jogador < computador:
        print("Computador ganhou!")

    else:
        print("Empate!")

    linha()

    

