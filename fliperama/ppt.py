# =========================================================
# Conceitos: modulo, lista, funcao com retorno e operador %
# Base: Jogo da Aula 17 (Atividade 11)
# Autor: [Pedro Noimann]
# Data: 2026.08.16
# =========================================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao

OPCOES = ['PEDRA', 'PAPEL', 'TESOURA']


def descobrir_vencedor(escolha_jogador, escolha_pc):
    if escolha_jogador == escolha_pc:
        return 'empate'

    proxima_jogada = (escolha_pc + 1) % 3

    if escolha_jogador == proxima_jogada:
        return 'jogador'

    return 'computador'


def exibir_opcoes():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()


def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    jogador_pontos = 0
    pc_pontos = 0

    while jogador_pontos != 2 and pc_pontos != 2:
        exibir_opcoes()

        escolha = ler_opcao(
            'Escolha sua jogada',
            ['0', '1', '2']
        )

        escolha = int(escolha)
        sorteio = randint(0, 2)

        print('Você jogou: ' + OPCOES[escolha])
        print('Computador jogou: ' + OPCOES[sorteio])

        vencedor = descobrir_vencedor(escolha, sorteio)

        if vencedor == 'empate':
            print('Deu empate!')

        elif vencedor == 'jogador':
            jogador_pontos += 1
            print('Você ganhou a rodada!')

        else:
            pc_pontos += 1
            print('O computador ganhou a rodada!')

        linha()
        print(
            f'Placar: Jogador {jogador_pontos} X '
            f'{pc_pontos} Computador'
        )
        linha()

    if jogador_pontos == 2:
        titulo('YOU WIN!')
    else:
        titulo('YOU LOSE!')

