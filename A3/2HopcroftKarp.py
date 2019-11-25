from GrafoListaAdjacencias import *

inf = 999999999

def HopcroftKarp(G):
    D = [inf] * G.qtdVertices()+1
    mate = [None] * G.qtdVertices()+1
    m = 0
    while BFS(G,mate,D)==True:
        for x in X # COMO SABER OS VERTICES QUE FAZEM PARTE DE X ??????
            if mate[x] == None:
                if DFS(G, mate, x, D)==True:
                    m = m+1
    return [m,mate]

def BFS(G,mate,D):
    Q = []
    for x in X:
        if mate[x] == None:
            D[x] = 0
            Q.append(x)
        else:
            D[x] = inf
    D[0] = inf
    while len(Q)>0:
        x = Q.pop(0)
        if D[x] < D[0]:
            for y in G.vizinhos_saintes(x):
                if D[mate[y]] == inf:
                    D[mate[y]] = D[x]+1
                    Q.append(mate[y])
    return D[0]

def DFS(G, mate, x, D):
    if x != None:
        for y in G.vizinhos_saintes(x):
            if D[mate[y]] == D[x]+1:
                if DFS(G,mate,mate[y],D)==True:
                    mate[y] = x
                    mate[x] = y
                    return True
        D[x] = inf
        return False
    return True
