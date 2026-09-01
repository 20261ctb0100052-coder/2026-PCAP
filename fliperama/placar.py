# Conceitos: modulo, lista, funcoes com retorno e arquivos
# Base: Jogo da Aula 17 (Atividade 11)
# Autor: [Pedro Noimann]
# Data: 2026.08.15

NOME_ARQUIVO = 'placar.csv'


def carregar_placar():
    try:
        arquivo = open(NOME_ARQUIVO, 'r')
        dados = arquivo.readline().strip()
        arquivo.close()

        numeros = dados.split(',')

        primeiro = int(numeros[0])
        segundo = int(numeros[1])
        terceiro = int(numeros[2])

        return [primeiro, segundo, terceiro]

    except FileNotFoundError:
        return [0, 0, 0]


def salvar_placar(placar):
    arquivo = open(NOME_ARQUIVO, 'w')

    primeiro = str(placar[0])
    segundo = str(placar[1])
    terceiro = str(placar[2])

    arquivo.write(primeiro + ',' + segundo + ',' + terceiro)

    arquivo.close()


def zerar_placar(placar):
    placar[0] = 0
    placar[1] = 0
    placar[2] = 0


