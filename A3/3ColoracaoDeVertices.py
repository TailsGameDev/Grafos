from GrafoListaAdjacencias import *

inf = 9999999999

def Lawler(G):
    X = [] * (2**G.qtdVertices() -1)
    X[0] = 0
    S = 2**G.qtdVertices()
    for s in S:
        s = f(S) # o que eh f ????????????????
        X[s] = inf
        #Gl = (S,{{u,v} in E: u,v E S}) ? # daqui para baixo não tive ânimo de tentar escrever direitinho
        for I in I(Gl) do
            i = f(S\I)
            if (X[i]+1)<X[s]:
                X[s] = X[i]+1
    return X[2**G.qtdVertices()-1]
