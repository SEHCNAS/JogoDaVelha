def PrintJogo(vetor):
    print(vetor[0] + '|' + vetor[1] + '|' + vetor[2])
    print('-----')
    print(vetor[3] + '|' + vetor[4] + '|' + vetor[5])
    print('-----')
    print(vetor[6] + '|' + vetor[7] + '|' + vetor[8])


if __name__ == '__main__':

    ContinuaJogo = True
    IdentificadorJogadorDoisValido = False
    vetor = [' '] * 9

    TiposJogadas = ['', '']
    Jogada = 0

    TiposJogadas[0] = input("Digite o identificador do primeiro jogador: ")

    while not IdentificadorJogadorDoisValido:
        TiposJogadas[1] = input("Digite o identificador do primeiro jogador: ")
        if TiposJogadas[1] != TiposJogadas[0]:
            IdentificadorJogadorDoisValido = True

    PrintJogo(vetor)

    while ContinuaJogo:

        posicao = int(input("Digite a casa em que deseja jogar: "))

        if vetor[posicao] == ' ':

            Jogada += 1
            if Jogada % 2 == 1:
                vetor[posicao] = TiposJogadas[0]
            else:
                vetor[posicao] = TiposJogadas[1]

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

        PrintJogo(vetor)

        if Jogada == 9:
            ContinuaJogo = False
