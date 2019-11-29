from GrafoListaAdjacencias import *
import copy
from conversor import *

def RedeResidual(G, caminho):
    Gl = Grafo(caminho, "dirigido")
    for u in range(1, G.qtdVertices() + 1):
        for v in range(1, G.qtdVertices() + 1):
            if G.getPeso(u, v) != G.naoTemArco:
                Gl.getArco(u, v).peso = G.getPeso(u, v)
                Gl.vertices[v].arcos.append(Arco(Gl.vertices[v], Gl.vertices[u], 0))
    return Gl

def EdmondsKarp(G, Gf):
    p = buscaEdmondsKarp(G, Gf)
    fluxo_maximo = 0
    while p != None:
        cf = 999999999
        for i in range(len(p) - 1):
            if Gf.getArco(p[i], p[i + 1]).peso < cf:
                cf = Gf.getArco(p[i], p[i + 1]).peso
        fluxo_maximo += cf
        for i in range(len(p) - 1):
            if G.getPeso(p[i], p[i + 1]) != G.naoTemArco:
                Gf.getArco(p[i + 1], p[i]).peso += cf
                Gf.getArco(p[i], p[i + 1]).peso -= cf
            else:
                print("%d" % p[i])
                Gf.getArco(p[i + 1], p[i]).peso -= cf
                Gf.getArco(p[i], p[i + 1]).peso += cf
        p = buscaEdmondsKarp(G, Gf)
    return fluxo_maximo


def buscaEdmondsKarp(G, Gf): # s eh o vertice em 1, por convenção
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
            if not C[v] and Gf.getPeso(u, v) > 0: # O QUE  EH F?????? Acho que eh o cf da rede residual
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

caminho = "db128.gr"
g = Grafo(caminho, "dirigido")
gr = RedeResidual(g, caminho)
fluxo_maximo = EdmondsKarp(g, gr)
print("Fluxo maximo: %d" % fluxo_maximo)
