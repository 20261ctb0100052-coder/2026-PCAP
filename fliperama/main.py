
#==============================================
# Arquivos:     main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Pedro Noimann
# Data:         2026.08.04
# Conceitos:
#==============================================

from telas import titulo, linha
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import (
    carregar_jogadores,
    menu_jogadores,
    salvar_jogadores
)
from ppt import jogar_ppt
from adivinhe import jogar_adivinhe
from parimpar import jogar_parimpar
from meujogo import jogar_meujogo


NOME_DO_DONO = 'Pedro Noimann'

OPCOES_MENU = ['0', '1', '2', '3', '4', '5', '6']

JOGOS = [
    'Adivinhe o Numero',
    'Pedra-Papel-Tesoura',
    'Par ou Impar',
    'Meu Jogo'
]


def menu_principal():
    titulo('FLIPERAMA')

    print('[1] Adivinhe o Numero')
    print('[2] Pedra-Papel-Tesoura')
    print('[3] Par ou Impar')
    print('[4] Jogadores')
    print('[5] Meu Jogo')
    print('[6] Placar')
    print('[0] Sair')

    linha()


def mostrar_placar(partidas):
    titulo('PLACAR')

    for posicao in range(len(JOGOS)):
        print(JOGOS[posicao] + ': ' + str(partidas[posicao]))

    linha()

    input('Pressione ENTER para voltar ao Fliperama...')


def iniciar():

    jogadores = carregar_jogadores()
    partidas = carregar_placar()

    while len(partidas) < 4:
        partidas.append(0)

    nome_jogador = input('Quem esta jogando? ')

    while True:

        menu_principal()

        escolha = ler_opcao(
            'Escolha uma opcao',
            OPCOES_MENU
        )

        if escolha == '0':
            salvar_jogadores(jogadores)
            salvar_placar(partidas)

            print('Obrigado por jogar, ' + nome_jogador + '!')
            break

        elif escolha == '1':
            jogar_adivinhe()

            partidas[0] += 1
            salvar_placar(partidas)

        elif escolha == '2':
            jogar_ppt()

            partidas[1] += 1
            salvar_placar(partidas)

        elif escolha == '3':
            jogar_parimpar()

            partidas[2] += 1
            salvar_placar(partidas)

        elif escolha == '4':
            menu_jogadores(jogadores)

        elif escolha == '5':
            jogar_meujogo()

            partidas[3] += 1
            salvar_placar(partidas)

        elif escolha == '6':
            mostrar_placar(partidas)


iniciar()
