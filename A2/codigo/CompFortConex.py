from GrafoListaAdjacencias import Grafo

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

    #isso resume as linhas 3 e 4 do algoritmo (o transpose)
    G.transpor()

    lista = indicesDosMenoresEmOrdem(F)


    [Ct,Tt,Alt,Ft] = dfs(G,lista)
    return Alt

def indicesDosMenoresEmOrdem(list):
    lista = [] # a ideia eh percorrer os tempos finais Fcopy, e sempre
    menor = float('inf') # pegar o menor e inserir no começo da 'lista'
    Fcopy = [] # com a finalidade de que a lista tenha os vertices decrescendo
    for k in range(len(list)):
        Fcopy.append(list[k])
    for i in range(len(list)-1): #pega o menor e insere no inicio
        Fcopy[0] = float('inf')
        menor = float('inf')
        idx=0;
        for k in range(len(Fcopy)):
            if (Fcopy[k]<menor):
                idx = k;
                menor = Fcopy[k]
        Fcopy[idx] = float('inf')
        lista.insert(0,idx)
    return lista

#testando montagem da lista de decrescentes
#sentinela = float('inf')
#print("indices: "+str(indicesDosMenoresEmOrdem([sentinela,4,2,3,1])))
# ----------- main abaixo

#grafo = Grafo("grafoDummy.txt","dirigido")
grafo = Grafo("grafocfc.txt","dirigido")
Alt = componentesFortementeConexas(grafo)
# montando lista com os conjuntos 'cfcs'
# a lógica eh ver quem nao antecede ninguem, depois ir percorrendo a partir dele.
antecedeAlguem = [False] * len(Alt)
for u in range (1,len(Alt)):
    if(Alt[u] != None):
        antecessor = Alt[u]
        antecedeAlguem[antecessor] = True
'''
quem nao antecede ninguem eh Meio Que A Raiz de um cfc,
entao vou percorrer ateh nao ter mais antecessor para montar
uma lista com todos os cfcs
'''
cfcs = []
for u in range (1,len(Alt)):
    if(not antecedeAlguem[u]):
        cfc = [u]
        a = Alt[u] #index do antecessor
        k = 10000
        while (a != None and k > 0):
            k-=1
            cfc.append(a)
            a = Alt[a]
        cfcs.append(cfc)

#montando output
for c in cfcs:
    s = ""
    for v in c:
        s = s + str(v) + ","
    s = s[:(len(s)-1)]
    print(s)
