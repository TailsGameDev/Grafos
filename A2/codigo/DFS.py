from Grafo import Grafo

def dfs(G, v, C, T, A, F, tempo):
    v -= 1
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]
    for u in G.vizinhos_saintes(v):
        u -= 1
        if not C[u]:
            A[u] = v
            dfs(G, u, C, T, A, F, tempo)
    tempo[0] += 1
    F[v] = tempo[0]
