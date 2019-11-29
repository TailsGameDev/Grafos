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
    D[0] = inf
    while len(Q) > 0:
        x = Q.pop(0)
        if D[x] < D[0]:
            for y in G.vizinhos(x):
                if D[mate[y]] == inf:
                    D[mate[y]] = D[x] + 1
                    Q.append(mate[y])
    return D[0]


def DFS(G, mate, x, D):
    if x != None:
        for y in G.vizinhos(x):
            if D[mate[y]] == D[x] + 1:
                if DFS(G, mate, mate[y], D) == True:
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = inf
        return False
    return True


G = Grafo("emparelhamento_maximo/gr128_10.gr")
[m, mate] = HopcroftKarp(G)
print(G.vertices)
