# -*- coding: utf-8 -*-
from Grafo import Grafo
import numpy

def floyd_warshall(grafo):
    # Inicializa a matriz inicial
    matriz_anterior = numpy.where(grafo.matriz == 0, float("inf"), grafo.matriz)
    for i in range(matriz_anterior.shape[0]):
        matriz_anterior[i][i] = 0
    for k in range(grafo.qtdVertices()):
    	# Inicializa uma nova matriz.
        matriz_atual = numpy.zeros((grafo.qtdVertices(), grafo.qtdVertices()))
        matriz_atual.fill(float("inf"))
        # Itera sobre todos os vertices grafo (existentes ou nao).
        for u in range(grafo.qtdVertices()):
            for v in range(grafo.qtdVertices()):
                # Realiza operacao de relaxamento.
                menor_distancia = min(matriz_anterior[u][v], matriz_anterior[u][k] + matriz_anterior[k][v])
                matriz_atual[u][v] = menor_distancia
                matriz_atual[v][u] = menor_distancia
        # Faz da matriz atual a matriz anterior da proxima iteracao.
        matriz_anterior = matriz_atual
    return matriz_atual

print("Insira o nome do arquivo contendo o grafo:")
caminho_do_grafo = input()
grafo = Grafo(caminho_do_grafo)
matriz_resultante = floyd_warshall(grafo)
for i in range(matriz_resultante.shape[0]):
    print("%d:" % i, end = "")
    print(str(matriz_resultante[i]).replace('[','').replace(".]","").replace(". ",","))