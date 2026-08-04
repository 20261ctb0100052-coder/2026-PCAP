#================================================
# Arquivos:     modulos.py
# Disciplina:   2026-PCAP
# Aula          20
# Autor:        Pedro Noimann
# Data:         2026.08.04
# Conceitos:
#==============================================

def ler_opçao(mensagem, validas):
    resposta = input(mensagem + ": ").strip()
    while resposta not in validas:
        print("Opção inválida! tente novamente.")
        resposta = input(mensagem + ": ").strip()
        return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
        return int(ler_opçao(mensagem, numeros))