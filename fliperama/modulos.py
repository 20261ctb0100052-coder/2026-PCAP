# Disciplina: 2026-PCAP
# Aula: 20
# Autor: []
# Data: 2026.08.08
# Conceitos: Reaproveitamento, validacao e funcoes

def ler_opcao(mensagem, opcoes_validas):
    """Le uma opcao ate que ela seja valida."""

    while True:
        resposta = input(mensagem + ': ').strip()

        if resposta in opcoes_validas:
            return resposta

        print('Opcao invalida! Tente novamente.')


def ler_numero(mensagem, minimo, maximo):
    """Le um numero inteiro dentro de um intervalo."""

    opcoes = []

    for numero in range(minimo, maximo + 1):
        opcoes.append(str(numero))

    resposta = ler_opcao(mensagem, opcoes)

    return int(resposta)


def ler_texto(mensagem):
    """Le um texto e impede que ele fique vazio."""

    while True:
        texto = input(mensagem + ': ').strip()

        if texto != '':
            return texto

        print('Nao pode ficar em branco! Tente novamente.')


