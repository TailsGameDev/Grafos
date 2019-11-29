# from GrafoListaAdjacencias import *
from GrafoEmparelhamento import Grafo

inf = 999999999


def HopcroftKarp(G):
    D = [inf] * (G.qtdVertices() + 1)
    mate = [None] * (G.qtdVertices() + 1)
    m = 0
    while BFS(G, mate, D) == True:
        for x in range(
            1, (G.qtdVertices() + 1) // 2
        ):  # COMO SABER OS VERTICES QUE FAZEM PARTE DE X ??????
            # por um arquivo percebi que sao os menores que a metade
            if mate[x] == None:
                if DFS(G, mate, x, D) == True:
                    m = m + 1
    return [m, mate]


def BFS(G, mate, D):
    Q = []
    for x in range(1, (G.qtdVertices() + 1) // 2):
        if mate[x] == None:
            D[x] = 0
            Q.append(x)
        else:
            D[x] = inf
    setD(D, None, inf)
    while len(Q) > 0:
        x = Q.pop(0)
        if getD(D, x) < getD(D, None):
            for y in G.vizinhos(x):
                if getD(D, mate[y]) == inf:
                    setD(D, mate[y], getD(D, x) + 1)  # D[mate[y]] = D[x] + 1
                    Q.append(mate[y])
    return D[0]


def getD(D, key):
    if key == None:
        return D[0]
    else:
        return D[key]


def setD(D, key, value):
    if key == None:
        D[0] = value
        if D[0] > inf:
            D[0] = inf  # nao ouso aumentar mais que o infinito
    else:
        D[key] = value
        if D[key] > inf:
            D[key] = inf  # nao ouso aumentar mais que o infinito


def DFS(G, mate, x, D):
    if x != None:
        for y in G.vizinhos(x):
            if getD(D, mate[y]) == getD(D, x) + 1:
                if DFS(G, mate, mate[y], D) == True:
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = inf
        return False
    return True


G = Grafo("emparelhamento_maximo/gr128_10.gr")
[m, mate] = HopcroftKarp(G)
print("valor do emparelhamento maximo: " + str(m))
print("\narestas pertencentes ao emparelhamento:")
for i in range(len(mate)):
    if mate[i] != None:
        print(str(i) + "-" + str(mate[i]))
