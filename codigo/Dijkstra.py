from GrafoListaAdjacencias import * # o grafo da matriz tava estranho com a funcao vizinhos
from heap import BinHeap

def Dijkstra(path,s):
    infinito = 999999999999

    grafo = Grafo(path)

    D=[None]; A = [None]; C = [None]; verticesIndex= [None]

    for v in range(1,grafo.qtdVertices()+1):
        D.append(infinito)
        A.append(None)
        C.append(False)
        #verticesIndex.append(v) #soh pra construir a heap

    D[s] = 0

    #monte = BinHeap()
    #monte.buildHeap(D[1::],verticesIndex[1::])

    C[0]=True # <- evitando um loop infinito

    while (False in C) :
        #argmin
        u = 1
        while(C[u]):
            u+=1
        for i in range(u,len(D)):
            if( (not C[i]) and (D[i]<D[u]) ):
                u = i

        C[u] = True

        Nu = grafo.vizinhos(u) # N de neighbors... vizinhos em ingles kk um troço assim
        for v in Nu:
            if ( (not C[v]) and D[v] > D[u] + grafo.peso(u,v)):
                D[v] = D[u] + grafo.peso(u,v)
                A[v] = u
                #aqui teria que atualizar o heap se fosse um heap

    return [D,A]

#funcao auxiliar pra imprimir a resposta
def caminhoAteh(inicio,final,A):
    if(inicio==final):
        return str(inicio)
    return caminhoAteh(inicio, A[final], A) + ',' + str(final)


s = 2

[D,A] = Dijkstra("grafo_teste_dijkstra.txt",s)

for v in range(1,len(D)):
    print( str(v) + ": " + caminhoAteh(s,v,A) + "; d=" + str(D[v]) )
