#==============================================
# Arquivos:     telas.py
# Disciplina:   2026-PCAP
# Aula          20
# Autor:        Pedro Noimann
# Data:         2026.08.04
# Conceitos:
#==============================================

# Definição da Moldura Caracteres e tamanho
CAR = "#"
TAM = 40

# Função para desenhar uma linha na tela
def linha():
    print(CAR * TAM)

# Função para desenhar um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
