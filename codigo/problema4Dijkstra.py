from GrafoListaAdjacencias import GrafoLA

infinito = 999999999999

grafo = GrafoLA("dijkstra.txt")

Dv=[]; Av = []; Cv = []

for i in range(grafo.qtdVertices()):
    Dv[i] = infinito
    Av[i] = None
    Cv[i] = False
