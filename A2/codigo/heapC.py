# peguei de https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html

'''
mas modifiquei, agora a heap tem chave e objeto! Dessa forma, podemos usar a
distancia como chave, e associar um objeto do tipo vertice, por exemplo.
'''

class Node:
    def __init__(self, obj, chave):
        self.vertice = obj
        self.peso = chave

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        self.posicoes = []

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i].peso < self.heapList[i // 2].peso:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
                self.posicoes[self.heapList[i].vertice] = i
                self.posicoes[self.heapList[i//2].vertice] = i//2
            i = i // 2

    def insert(self, vertice, peso):
        node = Node(vertice, peso)
        self.heapList.append(node)
        self.currentSize = self.currentSize + 1
        #caina 20/10 abaixo---
        while(len(self.posicoes)-1 < vertice):
            self.posicoes.append(-1) #-1 eh um valor invalido bizarro
        self.posicoes[vertice] = len(self.posicoes)
        #caina 20/10 acima----
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].peso > self.heapList[mc].peso:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
                self.posicoes[self.heapList[i].vertice] = i
                self.posicoes[self.heapList[mc].vertice] = mc
            i = mc

    #retorna o index do menor filho do nodo i
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].peso < self.heapList[i*2+1].peso:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1].vertice
        self.heapList[1] = self.heapList[self.currentSize]
        self.posicoes[self.heapList[self.currentSize].vertice] = 1
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, pesos):
        i = len(pesos) // 2
        self.currentSize = len(pesos)
        nodeList = []
        self.posicoes = [None]
        for i in range(len(pesos)):
            nodeList.append(Node(i + 1, pesos[i]))
            self.posicoes.append(i + 1)
        self.heapList = [Node(0, 0)] + nodeList[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
