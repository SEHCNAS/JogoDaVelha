def printJogo(vetor):
    print(vetor[0] + '|' + vetor[1] + '|' + vetor[2])
    print('-----')
    print(vetor[3] + '|' + vetor[4] + '|' + vetor[5])
    print('-----')
    print(vetor[6] + '|' + vetor[7] + '|' + vetor[8])


if __name__ == '__main__':

    ContinuaJogo = True
    IdentificadorJogadorDoisValido = False
    vetorExemplo = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    vetor = [' '] * 9

    TiposJogadas = ['', '']
    Jogada = 0

    TiposJogadas[0] = input("Digite o identificador do primeiro jogador: ")

    while not IdentificadorJogadorDoisValido:
        TiposJogadas[1] = input("Digite o identificador do primeiro jogador: ")
        if TiposJogadas[1] != TiposJogadas[0]:
            IdentificadorJogadorDoisValido = True

    print('Use o teclado numerico para escolher onde quer jogar.')
    printJogo(vetorExemplo)

    while ContinuaJogo:

        posicao = input("Digite a casa em que deseja jogar: ")
        if posicao.isnumeric():
            posicaoNum = int(posicao)
            if vetor[posicaoNum] == ' ':

                Jogada += 1
                if Jogada % 2 == 1:
                    vetor[posicaoNum] = TiposJogadas[0]
                else:
                    vetor[posicaoNum] = TiposJogadas[1]

            else:
                print('Ja existe valor nesse campo, jogue em outro casa!')

            if Jogada >= 5:
                for i in range(2):
                    # vencer na linha
                    if vetor[0] == TiposJogadas[i] and vetor[1] == TiposJogadas[i] and vetor[2] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    if vetor[3] == TiposJogadas[i] and vetor[4] == TiposJogadas[i] and vetor[5] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    if vetor[6] == TiposJogadas[i] and vetor[7] == TiposJogadas[i] and vetor[8] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    # Vencer na coluna
                    if vetor[0] == TiposJogadas[i] and vetor[3] == TiposJogadas[i] and vetor[6] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    if vetor[1] == TiposJogadas[i] and vetor[4] == TiposJogadas[i] and vetor[7] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    if vetor[2] == TiposJogadas[i] and vetor[5] == TiposJogadas[i] and vetor[8] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    # Vence em X
                    if vetor[2] == TiposJogadas[i] and vetor[4] == TiposJogadas[i] and vetor[6] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

                    if vetor[0] == TiposJogadas[i] and vetor[4] == TiposJogadas[i] and vetor[8] == TiposJogadas[i]:
                        print('O {Jogador}º jogador venceu'.format(Jogador=(i + 1)))
                        ContinuaJogo = False

            printJogo(vetor)

            if Jogada == 9:
                ContinuaJogo = False
        else:
            print('O valor digitado não é um numero valido. \n Escolha um numero de 0 a 8.')
