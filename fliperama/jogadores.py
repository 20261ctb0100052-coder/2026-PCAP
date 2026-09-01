from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto


ARQUIVO = 'jogadores.csv'


def cadastrar(jogadores):
    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espacos)').lower()

    posicao = buscar(jogadores, apelido)

    if posicao >= 0:
        print('Ja existe um jogador com esse apelido.')
        linha()
        return

    nome = ler_texto('Nome completo')
    jogadores.append([apelido, nome, '0'])

    print(f'Jogador {apelido} cadastrado com sucesso.')
    linha()


def listar(jogadores):
    titulo('TOP 10 JOGADORES')

    if not jogadores:
        print('Nenhum jogador cadastrado ainda.')
        linha()
        return

    ranking = sorted(
        jogadores,
        key=lambda jogador: int(jogador[2]),
        reverse=True
    )

    for posicao, jogador in enumerate(ranking[:10], start=1):
        apelido = jogador[0].ljust(6)
        nome = jogador[1].ljust(18)
        partidas = jogador[2].rjust(3)

        print(f'{str(posicao).rjust(2)}. {apelido} | {nome} | {partidas} partidas')

    linha()


def buscar(jogadores, apelido):
    for posicao, jogador in enumerate(jogadores):
        if jogador[0] == apelido:
            return posicao

    return -1


def alterar(jogadores):
    listar(jogadores)

    apelido = ler_texto('Apelido de quem vai mudar de nome').lower()
    posicao = buscar(jogadores, apelido)

    if posicao == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[posicao][1])

        nome_novo = ler_texto('Nome novo')
        jogadores[posicao][1] = nome_novo

        print('Pronto. Agora e ' + nome_novo + '.')

    linha()


def excluir(jogadores):
    titulo('EXCLUIR JOGADOR')

    apelido = ler_texto('Apelido de quem vai sair do cadastro').lower()
    posicao = buscar(jogadores, apelido)

    if posicao == -1:
        print('Nao achei ninguem com esse apelido.')
    else:
        print('Vou apagar o cadastro de ' + jogadores[posicao][1] + '.')
        print('[1] Confirmar')
        print('[2] Deixar como esta')

        escolha = ler_opcao('Sua escolha', ['1', '2'])

        if escolha == '1':
            jogadores.pop(posicao)
            print('Cadastro apagado.')
        else:
            print('Nada foi apagado.')

    linha()


def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(
            jogador[0] + ',' +
            jogador[1] + ',' +
            jogador[2] + '\n'
        )

    arquivo.close()


def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    jogadores = []

    for linha_lida in linhas:
        dados = linha_lida.strip().split(',')

        if len(dados) == 3:
            jogadores.append(dados)

    return jogadores


def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')

        print('[1] Cadastrar jogador')
        print('[2] Listar jogadores')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')

        linha()

        opcao = ler_opcao(
            'Sua escolha',
            ['0', '1', '2', '3', '4']
        )

        if opcao == '0':
            break

        if opcao == '1':
            cadastrar(jogadores)

        elif opcao == '2':
            listar(jogadores)

        elif opcao == '3':
            alterar(jogadores)

        elif opcao == '4':
            excluir(jogadores)


