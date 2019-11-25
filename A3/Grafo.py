# -*- coding: utf-8 -*-
import numpy
from conversor import converte

class Grafo:

    def __init__(self, caminho_do_arquivo=""):
        arquivo = open(converte(caminho_do_arquivo))
        titulo, vertices = arquivo.readline().split()
        vertices = int(vertices)
        self.rotulos = [None] * vertices
        self.matriz = numpy.zeros((vertices, vertices))
        self.arestas = 0
        for i in range(vertices):
            linha = arquivo.readline().split()
            indice = int(linha[0])
            linha.pop(0)
            self.rotulos[indice - 1] = " ".join(linha)
        arco_ou_aresta = arquivo.readline()
        while True:
            linha = arquivo.readline()
            if linha == "":
                break
            vertice1, vertice2, peso = linha.split()
            vertice1 = int(vertice1)
            vertice2 = int(vertice2)
            peso = float(peso)
            self.matriz[vertice1 - 1][vertice2 - 1] = peso
            if arco_ou_aresta == "*edges":
                self.matriz[vertice2 - 1][vertice1 - 1] = peso
            self.arestas += 1
        arquivo.close()

    def qtdVertices(self):
        return len(self.rotulos)

    def qtdArestas(self):
        return self.arestas

    def grau(self, vertice):
        grau = 0
        for i in range(self.matriz.shape[0]):
            if self.matriz[vertice - 1][i] != 0:
                grau += 1
        return grau

    def rotulo(self, vertice):
        return self.rotulos[vertice - 1]

    def vizinhos(self, vertice):
        return vizinhos_saintes(vertice)

    def vizinhos_saintes(self, vertice):
        lista_vizinhos = []
        for i in range(self.matriz.shape[0]):
            if self.matriz[vertice - 1][i] != 0:
                lista_vizinhos.append(i + 1)
        return lista_vizinhos

    def vizinhos_entrantes(self, vertice):
        lista_vizinhos = []
        for i in range(self.matriz.shape[0]):
            if self.matriz[i][vertice - 1] != 0:
                lista_vizinhos.append(i + 1)
        return lista_vizinhos

    def haAresta(self, vertice1, vertice2):
        return self.matriz[vertice1 - 1][vertice2 - 1] != 0

    def peso(self, vertice1, vertice2):
        if self.haAresta(vertice1, vertice2):
            return self.matriz[vertice1 - 1][vertice2 - 1]
        else:
            return float("inf")

    def transpor(self):
         self.matriz = self.matriz.transpose()
