#==============================================
# Arquivos:     main.py
# Disciplina:   2026-PCAP
# Aula          20
# Autor:        Pedro Noimann
# Data:         2026.08.04
# Conceitos:
#==============================================

# importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opçao

NOME_DO_DONO = "NOIMANN"
OPCOES = ["0", "1"]

while True:
    titulo("FFlIPERAMA DO " + NOME_DO_DONO)
    print("1 - Jogo Adivinhe o Número")
    print("0 - Sair do Fliperama")
    linha()
    opcao = ler_opçao("Escolha uma opção", OPCOES)

    if opcao == "0":
        print("Até a Próxima!")
        break
    elif opcao == "1":
        jogar_adivinhe()
    else:
        print("Opção Inválida! Tente novamente.")
