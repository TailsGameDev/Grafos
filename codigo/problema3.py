# algoritmo de Hierholzer

from Grafo import Grafo
import numpy

def Hierholzer(G): #grafo G = (V,E) V = Vertices, E = Edges (arestas)

    # C guarda informacao de que arestas foram visitadas
    # C usa uma linha e uma coluna em branco para fazer correspondencia
    # entre vertices e seus index
    C = numpy.zeros((G.qtdVertices()+1,G.qtdVertices()+1))

    # for atribui -1 a vertices nao visitados
    for i in range(G.qtdVertices()):
        for j in range(G.qtdVertices()):
            if (abs(G.matriz[i][j] - 1) < 0.01):
                C[i+1][j+1] = -1

    # v eh um vertice arbitrario. O primeiro vertice seria o de numero 1.
    v=1 # estou considerando que os vertices iniciais podem nao ter arestas
    while (G.qtdVertices()>=v and (not existeArestaNaoVisitada(G,v,C)) ):
        v+=1

    [r, Ciclo] = buscarSubcicloEuleriano(G,v,C)

    if (r == False):
        return [False, None]
    elif (-1 in C):
        return [False, None]
    else:
        return [True, Ciclo]

def buscarSubcicloEuleriano(G,v,C):
    Ciclo = [v]
    t = v
    #print("t: " +str(t))
    # Só prossegue se existir uma aresta não-visitada conectada aC i c l o.
    while(True):
        if(not existeArestaNaoVisitada(G,v,C)):
            return[False, None]
        else:
            u = VizinhoNaoVisitado(G,v,C)
            #print("v: "+str(v)+" u: "+str(u))

            C[v][u] = 1 # 1 eh True, -1 eh False, 0 eh nem tem aresta
            C[u][v] = 1 # marca seu correspondente tambem, para nao voltar

            #print(C)

            v = u
            Ciclo.append(v)
            #print(Ciclo)
        if(v == t):
            break

    #Para todo vértice x no Ciclo que tenha uma aresta adjacente não visitada
    for i in range(len(Ciclo)):
        if (existeArestaNaoVisitada(G,i,C)):
            [r,Ciclo2] = buscarSubcicloEuleriano(G,i,C)
            if (not r):
                return [False, None]
            #deu certo e achou mais um ciclo
            Ciclo[i:i] = Ciclo2[1:len(Ciclo2)] #insere sem repetir o inicial

    return [True, Ciclo]

def existeArestaNaoVisitada(G,v,C):
    # le a linha da matriz correspondente ao vertice
    for j in range(1,G.qtdVertices()+1):
        if (abs(C[v][j] + 1) < .01):
            #achou um vizinho nao visitado
            return True
    # todos os vizinhos foram visitados:
    return False

def VizinhoNaoVisitado(G,v,C):
    for j in range(1,G.qtdVertices()+1):
        if (abs(C[v][j] + 1) < .01):
            return j
    print("Chamou VizinhoNaoVisitado, mas nao existe nenhum!")
    return "bug"


G = Grafo("euleriano.txt")
[r, ciclo] = Hierholzer(G)
print(ciclo)
