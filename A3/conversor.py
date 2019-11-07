
def converte(caminho):
    with open(caminho) as f:
        txt = '*vertices '
        for line in f:
            #aqui voce tem acesso a cada linha line.
            linha = line.split()
            l0 = linha[0]
            if l0 == 'c':
                pass
            elif l0 == 'p':
                qtdVertices = int(linha[2])
                txt = txt + linha[2] + '\n'
                for v in range(qtdVertices):
                    txt = txt + str(v) + " " + str(v) + '\n'
                txt += '*edges\n'
            elif l0 == 'a':
                txt = txt + line[2:]
            if 'str' in line:
                break
        f = open('convertido.txt', 'r+')
        f.truncate(0)
        f.write(txt)
        f.close()
converte('instancia.gr')
