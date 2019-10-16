from Grafo import Grafo
from heap import BinHeap

def dfsVisit(G, v, C, T, A, F, tempo):
    #v -= 1
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]
    for u in G.vizinhos_saintes(v):
        #u -= 1
        if not C[u]:
            A[u] = v
            dfsVisit(G, u, C, T, A, F, tempo)
    tempo[0] += 1
    F[v] = tempo[0]

def dfs (G, lista):
    paraTodoV = G.qtdVertices()+1
    C = [False] * paraTodoV
    T = [float('inf')] * paraTodoV
    F = [float('inf')] * paraTodoV
    A = [None] * paraTodoV
    tempo = [0]
    for u in lista:
        if (not C[u]):
            dfsVisit(G,u,C,T,A,F,tempo)
    return [C, T, A, F]

def componentesFortementeConexas(G):
    lista = []
    for u in range(1,G.qtdVertices()+1):
        lista.append(u)
    [C, T, Al, F] = dfs(G,lista) #Alinha eh Ancestrais
    Gt = G #nem vamo usar G depois #copy.deepcopy(G)

    #isso resume as linhas 3 e 4 do algoritmo (o transpose)
    Gt.matriz = Gt.matriz.transpose()

    # para pegar a ordem crescente usei heap, mas deu um erro dai fui p lista
    '''
    heap = BinHeap()
    for u in range(1,len(F)):
        heap.insert(u, F[u])
    lista = []
    for u in range(1,len(F)):
        lista.insert(0,heap.delMin())
    '''

    lista = []
    Fcopy = []
    for k in range(len(F)):
        Fcopy.append(F[k])

    for i in range(len(F)): #pega o menor e insere no inicio
        Fcopy[0] = float('inf')
        menor = Fcopy[0]
        idx=0;
        for k in range(len(Fcopy)):
            if (Fcopy[k]<menor):
                idx = k;
                menor = Fcopy[k]
                Fcopy[k] = float('inf')
        lista.insert(0,idx)

    [Ct,Tt,Alt,Ft] = dfs(G,lista)
    return Alt

grafo = Grafo("grafoTeste1.txt")
Alt = componentesFortementeConexas(grafo)

# montando lista com os conjuntos 'cfcs'
# a lógica eh ver quem nao antecede ninguem, depois ir percorrendo a partir dele.
antecedeAlguem = [False] * len(Alt)
for u in range (1,len(Alt)):
    if(Alt[u] != None):
        antecessor = Alt[u]
        antecedeAlguem[antecessor] = True
cfcs = []
for u in range (1,len(Alt)):
    if(not antecedeAlguem): #ehMeioQueARaiz
        cfc = [u]
        a = Alt[u] #index do antecessor
        k = 10000
        while (a != None and k > 0):
            k-=1
            cfc.append(a)
            a = Alt[a]
        cfcs.append(cfc)

#montando output
print(cfcs)
