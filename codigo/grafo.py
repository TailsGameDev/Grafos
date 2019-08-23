# -*- coding: utf-8 -*-
import numpy

class Grafo:

    def __init__(self, arquivo):
        file = open(arquivo)
        titulo, vertices = file.readline().split()
        vertices = int(vertices)
        self.rotulos = [None] * vertices
        self.matriz = numpy.zeros((vertices, vertices))
        self.arestas = 0
        for i in range(vertices):
            indice, rotulo = file.readline().split(" \"")
            indice = int(indice)
            self.rotulos[indice - 1] = rotulo.replace("\"\n", "")
        file.readline()
        while True:
            line = file.readline()
            if line == "":
                break
            vertice1, vertice2, peso = line.split()
            vertice1 = int(vertice1)
            vertice2 = int(vertice2)
            peso = float(peso)
            self.matriz[vertice1 - 1][vertice2 - 1] = peso
            self.arestas += 1
        file.close()

    def qtdVertices(self):
        return len(self.rotulos)
    
    def qtdArestas(self):
        return self.arestas

    def grau(self, vertice):
        grau = 0
        for i in range(self.matriz.shape[0]):
            grau += self.matriz[vertice - 1][i]
        return grau
    
    def rotulo(self, vertice):
        return self.rotulos[vertice - 1]

    def vizinhos(self, vertice):
        lista_vizinhos = []
        for i in range(self.matriz.shape[0]):
            if self.matriz[vertice - 1][i] == 1.0:
                lista_vizinhos.append(i + 1)
        return lista_vizinhos

    def haAresta(self, vertice1, vertice2):
        return self.matriz[vertice1 - 1][vertice2 - 1] != 0

    def peso(self, vertice1, vertice2):
        if self.haAresta(vertice1, vertice2):
            return self.matriz[vertice1 - 1][vertice2 - 1]
        else:
            return float("inf")