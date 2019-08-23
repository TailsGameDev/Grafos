# -*- coding: utf-8 -*-
import queue
from Grafo import Grafo

def busca_em_largura(grafo, vertice_inicial):
    lista_de_visitados = [False] * grafo.qtdVertices()
    lista_de_distancias = [float("inf")] * grafo.qtdVertices()
    ancestrais = [None] * grafo.qtdVertices()
    lista_de_visitados[vertice_inicial - 1] = True
    lista_de_distancias[vertice_inicial - 1] = 0
    fila = queue.Queue(maxsize=grafo.qtdVertices())
    fila.put(vertice_inicial - 1)
    while not fila.empty():
        vertice_atual = fila.get()
        vizinhos = grafo.vizinhos(vertice_atual + 1)
        for k in vizinhos:
            if not bool(lista_de_visitados[k - 1]):
                lista_de_visitados[k - 1] = True
                lista_de_distancias[k - 1] = lista_de_distancias[vertice_atual] + 1
                ancestrais[k - 1] = vertice_atual
                fila.put(k - 1)

    return (lista_de_distancias, ancestrais)

print("Insira o nome do arquivo contendo o grafo:")
caminho_do_grafo = input()
grafo = Grafo(caminho_do_grafo)
lista_de_distancias = busca_em_largura(grafo, 2)[0]
i = 0
restantes = len(lista_de_distancias)
print("Resultado da busca em largura:")
while i < len(lista_de_distancias) and restantes > 0:
    vertices = []
    for j in range(len(lista_de_distancias)):
        if lista_de_distancias[j] == i:
             vertices.append(j + 1)
             restantes -= 1
    if len(vertices) > 0:
        print("%d: " % i, end="")
        print(*vertices, sep=", ")
    i += 1

    