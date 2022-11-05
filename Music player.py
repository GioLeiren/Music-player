músicas = []
tocadas = []
tocando = []
comandos = []
resposta = []
musica = 0
play = 0

while True:
    opção = []
    opção.extend(map(str, input().split()))
    if opção[0] == 'add':
        comandos.append(opção)
        músicas.append(opção[1])
    elif opção[0] == 'del':
        if len(tocando) != 0:              #tem algo tocando
            if opção[1] != tocando[0]:
                if opção[1] in músicas:
                    opção.append(músicas.index(opção[1]))        #coloca a posição do negocio removido em opção pra ir pros comandos
                    comandos.append(opção)
                    músicas.remove(opção[1])
        else:
            if opção[1] in músicas:
                opção.append(músicas.index(opção[1]))  # coloca a posição do negocio removido em opção pra ir pros comandos
                comandos.append(opção)
                músicas.remove(opção[1])
    elif opção[0] == 'play':
        comandos.append(opção)
        if len(músicas) != 0:
            tocando.append(músicas[musica])
        play = 1
    elif opção[0] == 'stop':
        if len(tocando) != 0:
            tocando = []
    elif opção[0] == 'current':
        if len(tocando) != 0:
            resposta.append(tocando[0])
        else:
            if len(músicas) != 0:
                if len(músicas) == 1:
                    resposta.append(músicas[0])
                else:
                    resposta.append(músicas[musica])
            else:
                resposta.append('Toque! Toque, Dijê!')
    elif opção[0] == 'ended':
        comandos.append(['ended'])
        if len(tocando) != 0:
            tocando.pop(0)
            if len(músicas) != 0:
                musica += 1
                if musica < len(músicas):
                    tocando.append(músicas[musica])
                else:
                    musica = 0
                    tocando.append(músicas[musica])

    elif opção[0] == 'next':
        if len(tocando) != 0:
            if opção[1] in músicas and opção[1] != tocando[0]:
                opção.append(músicas.index(opção[1]))
                comandos.append(opção)
                músicas.remove(opção[1])  #tira a musica da posiçao q ela ta e põe no inicio
                músicas.insert(1, opção[1])
        else:
            if opção[1] in músicas:
                músicas.remove(opção[1])  # tira a musica da posiçao q ela ta e põe no inicio
                músicas.insert(0, opção[1])
    elif opção[0] == 'list':
        if len(músicas) != 0:
            palavra_demoniaca = ''
            for c in range(0, len(músicas)):
                if c == len(músicas) - 1:
                    palavra_demoniaca += músicas[c]
                    resposta.append(palavra_demoniaca)
                else:
                    palavra_demoniaca += músicas[c] + ','
        else:
            resposta.append('[vazia]')
    elif opção[0] == 'undo':
        if len(opção) == 1:
            if len(comandos) != 0:
                if comandos[-1][0] == 'add':
                    músicas.remove(comandos[-1][1])
                elif comandos[-1][0] == 'del':
                    músicas.insert(comandos[-1][2], comandos[-1][1])
                elif comandos[-1][0] == 'next':
                    músicas.remove(comandos[-1][1])
                    músicas.insert(comandos[-1][2], comandos[-1][1])
                elif comandos[-1][0] == 'play':
                    'a'
                comandos.pop()
        else:
            if len(comandos) != 0:
                for c in range(len(comandos) - 1, -1, -1):
                    if comandos[-1][0] == 'add':
                        if len(tocando) != 0:  # tem algo tocando
                            if comandos[-1][1] != tocando[0]:
                                if comandos[-1][1] in músicas:
                                    músicas.remove(comandos[-1][1])
                        else:
                            if comandos[-1][1] in músicas:
                                músicas.remove(comandos[-1][1])
                    elif comandos[-1][0] == 'ended':
                        if play == 1:
                            break
                    elif comandos[-1][0] == 'del':
                        músicas.insert(comandos[-1][2], comandos[-1][1])
                    elif comandos[-1][0] == 'next':
                        músicas.remove(comandos[-1][1])
                        músicas.insert(comandos[-1][2], comandos[-1][1])
                    elif comandos[-1][0] == 'play':
                        tocando = []
                    comandos.pop()
    elif opção[0] == 'fight':
        resposta.append('Jedi Wagner, assuma o comando!')
        break
for te_odeio in resposta:
    print(te_odeio)