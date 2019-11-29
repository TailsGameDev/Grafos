class Grafo:
    def __init__(self, path):
        file = open(path)
        line = file.readline()
        self.vertices = []
        while line:
            if line[0] == "c":
                pass
            elif line[0] == "p":
                x1, x2, maxVertice, x4 = line.split()
                for i in range(int(maxVertice) + 1):
                    self.vertices.append([])
            elif line[0] == "e":
                e, vX, vY = line.split()
                self.vertices[int(vX)].append(int(vY))
                self.vertices[int(vY)].append(int(vX))
            line = file.readline()

    def qtdVertices(self):
        return len(self.vertices) - 1

    def vizinhos(self, u):
        return self.vertices[u]


G = Grafo("emparelhamento_maximo/gr128_10.gr")
