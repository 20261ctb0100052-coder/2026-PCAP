#==============================================
# Arquivos:     adivinhe.py
# Disciplina:   2026-PCAP
# Aula          20
# Autor:        Pedro Noimann
# Data:         2026.08.04
# Conceitos:
#==============================================

from random import randint
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NÚMERO')
    print('Adivinhe o número que foi escolhido entre 1 e 10.')

    numero_secreto = randint(1, 10)
    quantidade_tentativas = 0

    while True:
        tentativa = ler_numero('Qual é o seu palpite?', 1, 10)
        quantidade_tentativas += 1

        if tentativa == numero_secreto:
            break

        if tentativa < numero_secreto:
            print('O número secreto é maior. Tente novamente.')
        else:
            print('O número secreto é menor. Tente novamente.')

    linha()
    print(
        f'Parabéns! Você acertou o número secreto '
        f'{numero_secreto} em {quantidade_tentativas} tentativas.'
    )


