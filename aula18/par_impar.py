# ============================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Pedro Noimann
# Data       : 25/06/2026
# ════════════════════════════════════════════════════════════

import random

jogador = 0
maquina = 0

while jogador < 3 and maquina < 3:

    aposta = input("Escolha par (p) ou ímpar (i): ")

    while aposta != "p" and aposta != "i":
        aposta = input("Digite apenas p ou i: ")

    numero_jogador = int(input("Escolha um número de 0 a 5: "))

    while numero_jogador < 0 or numero_jogador > 5:
        numero_jogador = int(input("Número inválido! Digite de 0 a 5: "))

    numero_maquina = random.randint(0, 5)

    soma = numero_jogador + numero_maquina

    print("Você jogou:", numero_jogador)
    print("Máquina jogou:", numero_maquina)
    print("Soma:", soma)

    if soma % 2 == 0:
        resultado = "p"
        print("Resultado: Par")
    else:
        resultado = "i"
        print("Resultado: Ímpar")

    if aposta == resultado:
        print("Você venceu a rodada!")
        jogador = jogador + 1
    else:
        print("A máquina venceu a rodada!")
        maquina = maquina + 1

    print("Você:", jogador)
    print("Máquina:", maquina)

if jogador == 3:
    print("Parabéns! Você venceu o jogo!")
else:
    print("A máquina venceu o jogo!")