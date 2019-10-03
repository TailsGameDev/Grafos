from GrafoListaAdjacencias import *
from heap import BinHeap

def Dijkstra(grafo, vertice_inicial):

    D=[None]; A = [None]; C = [None]; verticesIndex = [None]

    for v in range(grafo.qtdVertices()):
        D.append(float("inf"))
        A.append(None)
        C.append(False)

    D[vertice_inicial] = 0

    monte = BinHeap()
    monte.buildHeap(D[1:])

    C[0] = True # <- evitando um loop infinito

    while False in C:
        #argmin
        u = monte.delMin()
        C[u] = True
        
        vizinhos = grafo.vizinhos(u)
        for v in vizinhos:
            if (not C[v]) and D[v] > D[u] + grafo.peso(u,v):
                D[v] = D[u] + grafo.peso(u,v)
                A[v] = u
                monte.heapList[monte.posicoes[v]].peso = D[u] + grafo.peso(u,v)
                monte.percUp(monte.posicoes[v])

    return (D,A)

#funcao auxiliar pra imprimir a resposta
def caminhoAte(inicio,final,A):
    if(inicio == final):
        return str(inicio)
    return caminhoAte(inicio, A[final], A) + ',' + str(final)

print("Insira o nome do arquivo contendo o grafo:")
caminho_do_grafo = input()
print("Insira o vertice inicial:")
vertice_inicial = int(input())
grafo = Grafo(caminho_do_grafo)
(D, A) = Dijkstra(grafo, vertice_inicial)

for v in range(1,len(D)):
    if D[v] != float("inf"):
        print(str(v) + ": " + caminhoAte(vertice_inicial,v,A) + "; d=" + str(D[v]))
    else:
        print(str(v) + ": " + "; d=" + str(D[v]))
