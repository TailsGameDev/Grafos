from Grafo import Grafo

def dfsVisit(G, v, C, T, A, F, tempo):
    v -= 1
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]
    for u in G.vizinhos_saintes(v):
        u -= 1
        if not C[u]:
            A[u] = v
            dfsVisit(G, u, C, T, A, F, tempo)
    tempo[0] += 1
    F[v] = tempo[0]

def dfs (G, lista):
    paraTodoV = G.qtdVertices()
    C = [False] * paraTodoV
    T = [float('inf')] * paraTodoV
    F = [float('inf')] * paraTodoV
    A = [None] * paraTodoV
    tempo = [0]
    for u in lista:
        if not C[u]:
            dfsVisit(G,u,C,T,A,F,tempo)
    return [C, T, A, F]

def componentesFortementeConexas(G):
    lista = []
    k=0
    for u in range(G.qtdVertices()):
        lista.append(k)
        k+=1
    [C, T, A_linha, F] = dfs(G,lista) #Alinha eh Ancestrais
    Gt = copy.deepcopy(G)
    Gt.matriz = Gt.matriz.transpose()
    #isso resume as linhas 3 e 4 do algoritmo
