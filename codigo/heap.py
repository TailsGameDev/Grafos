# peguei de https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html

'''
mas modifiquei, agora a heap tem chave e objeto! Dessa forma, podemos usar a
distancia como chave, e associar um objeto do tipo vertice, por exemplo.
'''

class Node:
    def __init__(self, key, object):
        self.key = key
        self.object = object

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i].key < self.heapList[i // 2].key:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,key, object=None):
        if (object==None):
            object = key
        node = Node(key, object)
        self.heapList.append(node)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i].key > self.heapList[mc].key:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    #retorna o index do menor filho do nodo i
    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2].key < self.heapList[i*2+1].key:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1].object
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,keyList, objList=[]):
        if (objList == []):
            objList = keyList
        i = len(keyList) // 2
        self.currentSize = len(keyList)

        nodeList=[]
        for i in range(len(keyList)):
            nodeList.append(Node(keyList[i],objList[i]))

        self.heapList = [0] + nodeList[:]
        while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([1,2,3,4,5],['a','b','c','d','e'])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
