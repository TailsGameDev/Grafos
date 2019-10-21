from Grafo import Grafo

def OrdenacaoTopologica(G):
    C = [False] * G.qtdVertices()
    T = [float("inf")] * G.qtdVertices()
    F = [float("inf")] * G.qtdVertices()
    # Tempo de inicio
    tempo = [0]
    # Lista de vertices ordenados
    O = []
    for u in range(1, G.qtdVertices() + 1):
        if not C[u - 1]:
            dfsVisitOT(G, u, C, T, F, tempo, O)
    return O

def dfsVisitOT(G, v, C, T, F, tempo, O):
    v -= 1
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]
    for u in G.vizinhos_saintes(v + 1):
        if not C[u - 1]:
            dfsVisitOT(G, u, C, T, F, tempo, O)
    tempo[0] += 1
    F[v] = tempo[0]
    O.insert(0, v + 1)


grafo = Grafo("GrafoOrdenacaoTopologica.txt")
ordenado = OrdenacaoTopologica(grafo)
rotulos = []
for i in ordenado:
    rotulos.append(grafo.rotulo(i)[1:len(grafo.rotulo(i)) - 1])

print(*rotulos, sep=" -> ")