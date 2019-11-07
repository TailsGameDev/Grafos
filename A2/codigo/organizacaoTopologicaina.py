from GrafoListaAdjacencias import Grafo

def DFSParaOrdenacaoTopologica(G):
    paraTodoV = G.qtdVertices()+1
    C = [False] * paraTodoV
    T = [float('inf')] * paraTodoV
    F = [float('inf')] * paraTodoV
    tempo = [0]
    O = []
    for u in range(1,G.qtdVertices()):
        if (C[u]==False):
            DFSVisitOT(G,u,C,T,F,tempo,O)
    return O

def DFSVisitOT(G,v,C,T,F,tempo,O):
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]
    for u in G.vizinhos_saintes(v):
        if C[u]==False:
            DFSVisitOT(G,u,C,T,F,tempo,O)
    tempo[0] += 1
    F[v] = tempo[0]
    O.insert(0,v)

G = Grafo("grafoDummyOrganizacao.txt","dirigido")
O = DFSParaOrdenacaoTopologica(G)

s = ""
for v in range(len(O)-1):
    s = s + G.rotulo(O[v]) + "->"
s = s + G.rotulo(O[len(O)-1]) + "."
print(s)
