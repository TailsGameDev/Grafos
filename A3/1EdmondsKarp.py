from GrafoListaAdjacencias import *
import copy
from conversor import *

def RedeResidual(G):
    Gl = copy.deepcopy(G)
    for u in range(1,G.qtdVertices() + 1):
        for v in range(1,G.qtdVertices() + 1):
            if G.peso(u,v) != G.naoTemArco:
                Gl.vertices[v].arcos.append(Arco(Gl.vertices[v],Gl.vertices[u],G.peso(u,v)))
                Gl.getArco(u,v).peso = 0

    return Gl

def EdmondsKarp(G, Gf = "deixaQueMontaNoConstrutor"): # s eh o vertice em 1, por convenção
    if Gf == "deixaQueMontaNoConstrutor":
        Gf = RedeResidual(G)
    C = [False] * (G.qtdVertices() + 1)
    A = [None] * (G.qtdVertices() + 1)
    C[1] = True
    Q = [] #tentando meter uma lista ver se resolve
    Q.append(1)
    while (len(Q) > 0):
        u = Q.pop(0)
        vizinhos_saintes = G.vizinhos_saintes(u)
        for v in vizinhos_saintes:
            if C[v]==False and ((G.peso(u,v)-Gf.peso(u,v))>0): # O QUE  EH F?????? Acho que eh o cf da rede residual
                C[v] = True
                A[v] = u
                t = len(G.vertices)-1
                if v == t: #O QUE EH t?????
                    p = [t]
                    w = t
                    while w != s:
                        w = A[w]
                        p.append(w)
                    return p
                Q.append(v)
    return None

# converte("instancia.txt")
g = Grafo("instancia.txt")
print("%d", EdmondsKarp(g))
