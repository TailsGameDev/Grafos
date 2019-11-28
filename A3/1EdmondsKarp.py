from GrafoListaAdjacencias import *
import copy
from conversor import *

def RedeResidual(G):
    # Gl = copy.deepcopy(G)
    Gl = Grafo("db128.gr", "dirigido")
    for u in range(1, G.qtdVertices() + 1):
        for v in range(1, G.qtdVertices() + 1):
            if G.getPeso(u, v) != G.naoTemArco:
                if Gl.getPeso(v, u) == G.naoTemArco:
                    Gl.vertices[v].arcos.append(Arco(Gl.vertices[v], Gl.vertices[u], G.getPeso(u, v)))
                    Gl.getArco(u, v).peso = 0
                else:
                    Gl.getArco(v, u).peso = G.getPeso(u, v) - Gl.getPeso(u, v)

    return Gl

def EdmondsKarp2(G):
    Gf = RedeResidual(G)
    p = EdmondsKarp(G, Gf)
    while p != None:
        print(p)
        cf = 999999999
        for i in range(len(p) - 1):
            if Gf.getArco(p[i + 1], p[i]).peso < cf:
                cf = Gf.getArco(p[i + 1], p[i]).peso
        print("cf %d" % cf)
        for i in range(len(p) - 1):
            if G.getPeso(p[i], p[i] + 1) != G.naoTemArco:
                G.getArco(p[i], p[i] + 1).peso += cf
            else:
                G.getArco(p[i], p[i] + 1).peso -= cf
        print("pdg %d" % G.getPeso(1, 128))
        Gf = RedeResidual(G)
        print("pdr %d" % Gf.getPeso(128, 1))
        p = EdmondsKarp(G, Gf)


def EdmondsKarp(G, Gf = "deixaQueMontaNoConstrutor"): # s eh o vertice em 1, por convenção
    if Gf == "deixaQueMontaNoConstrutor":
        Gf = RedeResidual(G)
    s = 1
    t = len(G.vertices) - 1
    C = [False] * (G.qtdVertices() + 1)
    A = [None] * (G.qtdVertices() + 1)
    C[s] = True
    Q = [] #tentando meter uma lista ver se resolve
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        vizinhos_saintes = G.vizinhos_saintes(u)
        for v in vizinhos_saintes:
            if not C[v] and ((G.getPeso(u, v) - Gf.getPeso(u, v))>0): # O QUE  EH F?????? Acho que eh o cf da rede residual
                C[v] = True
                A[v] = u
                if v == t:
                    p = [t]
                    w = t
                    while w != s:
                        w = A[w]
                        p.insert(0, w)
                    return p
                Q.append(v)
    return None

# converte("instancia.txt")
g = Grafo("db128.gr", "dirigido")
EdmondsKarp2(g)
# resultado = EdmondsKarp(g)
# print(resultado)