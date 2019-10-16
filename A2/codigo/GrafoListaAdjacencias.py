class Grafo:
    def __init__(self, caminho_do_arquivo, dirigido="dirigido"):
        arquivo = open(caminho_do_arquivo)
        titulo, vertices = arquivo.readline().split()
        vertices = int(vertices)

        self.vqtdVertices = vertices

        self.vertices = [None] * (vertices+1)

        for i in range(1,vertices+1):
            line = arquivo.readline().split()
            numero = int(line[0])
            rotulo = " ".join(line[1:])
            vertice = Vertice(numero, rotulo)
            self.vertices[i] = vertice


        linha = arquivo.readline() #deveria ser a linha que diz "*edges"
        linha = arquivo.readline()
        self.vqtdArestas = 0

        while (linha):
            v1, v2, peso = linha.split()
            v1 = int(v1); v2 = int(v2); peso = float(peso)
            self.vertices[v1].arcos.append(Arco(self.vertices[v1],self.vertices[v2], peso))
            if(dirigido == "dirigido"):
                self.vertices[v2].arcos.append(Arco(self.vertices[v2],self.vertices[v1], peso))
            self.vqtdArestas += 1
            linha = arquivo.readline()

        arquivo.close()

    def qtdVertices(self):
        return self.vqtdVertices

    def qtdArestas(self):
        return self.vqtdArestas


    # vertice pode ser tratado como numero ou objeto, e dah uma resposta equivalente
    def grau(self, v):
        if(isinstance(v,int)):
            return len(self.vertices[v].arcos)
        else:
            len(v.arcos)

    def rotulo(self, v):
        if(isinstance(v,int)):
            return self.vertices[v].rotulo
        else:
            v.rotulo

    def vizinhos(self, v):
        ehInt = isinstance(v,int)
        if(ehInt):
            v = self.vertices[v]
        vizinhos = []
        numVizinhos = []
        for i in range(len(v.arcos)):
            vizinhos.append(v.arcos[i].destino)
            numVizinhos.append(v.arcos[i].destino.numero)

        if(ehInt):
            return numVizinhos
        else:
            return vizinhos

    def vizinhos_saintes(self, v):
        return self.vizinhos(v)

    def haAresta(self, u, v):
        if(isinstance(v,int)):
            v = self.vertices[v]; u = self.vertices[u]

        for i in range(len(v.arcos)):
            if (v.arcos[i].destino == u):
                return True

        return False

    def peso(self, u, v):
        if(isinstance(v,int)):
            v = self.vertices[v]; u = self.vertices[u]

        for i in range(len(v.arcos)):
            if (v.arcos[i].destino == u):
                return v.arcos[i].peso
        return 999999999999

class Vertice:
    def __init__(self, numero, rotulo):
        self.numero = numero
        self.rotulo = rotulo
        self.visitado = False
        self.arcos = []

class Arco:
    def __init__(self, v1, v2, peso = 1):
        self.origem = v1
        self.destino = v2
        self.peso = peso
        self.visitado = False
