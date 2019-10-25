from GrafoListaAdjacencias import *
from heapC import BinHeap

def Kruskal(G):
    A = []
    S = [[]] * (G.qtdVertices()+1)

    for v in range(1,G.qtdVertices()+1):
        S[v] = [v]

    arcos = G.getArcos()
    heap =  BinHeap()
    for a in range(len(arcos)):
        heap.insert(a, arcos[a].peso)
        #print(list(map(lambda nodo: 0 if nodo==0 else nodo.vertice ,heap.heapList)))
        #print(heap.posicoes)
    El = []
    for a in range(len(arcos)):
        El.append(arcos[heap.delMin()])
    for ark in El:
        u = ark.origem.numero
        v = ark.destino.numero
        #print(S)
        #print("u: "+str(u)+"; v: "+str(v))
        if (S[u] != S[v]):
            if(not ark in A):
                A.append(ark) # A <- A U {{u,v}}
            x = S[u]
            for s in S[v]:
                if(not s in x):
                    x.append(s) #x <- S[u] U S[v]
            for w in x:
                S[w] = x
    return A

 #nao eh dirigido, mas no algoritmo funciona. se eh nao dirigido tem uma Aresta
 #para ir e uma para voltar :(
G = Grafo("grafoDummyTree.txt","dirigido")
A = Kruskal(G)
soma = 0
for a in A:
    soma += a.peso
print(soma)
l = (list(map(lambda a: str(a.origem.numero)+"-"+str(a.destino.numero)+",",A)))
ans = ""
for i in range(len(l)):
    ans = ans + l[i]
print(ans[:len(ans)-1])
