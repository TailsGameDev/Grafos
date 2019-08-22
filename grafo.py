# -*- coding: utf-8 -*-
import numpy

class Grafo:

    def __init__(self, arquivo):
        file = open(arquivo)
        titulo, vertices = file.readline().split()
        vertices = int(vertices)
        self.rotulos = [None] * vertices
        self.matriz = numpy.zeros((vertices, vertices))
        for i in range(vertices):
            indice, rotulo = file.readline().split(" \"")
            indice = int(indice)
            print(indice)
            self.rotulos[indice - 1] = rotulo
        file.readline()
        try:
            while True:
                vertice1, vertice2, peso = file.readline().split()
                vertice1 = int(vertice1)
                vertice2 = int(vertice2)
                peso = float(peso)
                print(vertice2)
                self.matriz[vertice1 - 1][vertice2 - 1] = peso
        except EOFError:
           print("Erro")

grafo = Grafo("facebook_santiago.net")
print(grafo.matriz)
