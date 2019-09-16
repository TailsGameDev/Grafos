# -*- coding: utf-8 -*-
import queue
from Grafo import Grafo

def busca_em_largura(grafo, vertice_inicial):
    # Desloca o vertice inicial de acordo com o padrao utilizado na classe grafo.
    vertice_inicial -= 1
    # Inicializa as estruturas basicas.
    lista_de_visitados = [False] * grafo.qtdVertices()
    lista_de_distancias = [float("inf")] * grafo.qtdVertices()
    ancestrais = [None] * grafo.qtdVertices()
    # Inicializa condicoes do vertice inicial.
    lista_de_visitados[vertice_inicial] = True
    lista_de_distancias[vertice_inicial] = 0
    # Cria fila com os vertices e adiciona o vertice inicial.
    fila = queue.Queue(maxsize=grafo.qtdVertices())
    fila.put(vertice_inicial)
    # Visita todos os vertices
    while not fila.empty():
    	# Pega o proximo vertice da fila e seus vizinhos.
        vertice_atual = fila.get()
        vizinhos = grafo.vizinhos(vertice_atual + 1)
        # Visita todos os vizinhos do vertice escolhido.
        for k in vizinhos:
        	# Desloca o vizinho atual de acordo com o padrao utilizado na classe grafo
            k -= 1
            # Se o vizinho atual ainda não foi visitado...
            if not bool(lista_de_visitados[k]):
            	# Marca-o como visitado,
                lista_de_visitados[k] = True
                # Define a distancia da origem ate ele,
                lista_de_distancias[k] = lista_de_distancias[vertice_atual] + 1
                # Define o vertice atual como seu ancestral,
                ancestrais[k] = vertice_atual
                # E coloca-o na fila.
                fila.put(k)
    # Retorna um par ordenado com a lista de distancias e a de ancestrais.
    return (lista_de_distancias, ancestrais)

print("Insira o nome do arquivo contendo o grafo:")
caminho_do_grafo = input()
print("Insira o vertice inicial:")
vertice_inicial = int(input())
grafo = Grafo(caminho_do_grafo)
lista_de_distancias = busca_em_largura(grafo, vertice_inicial)[0]
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
        print(*vertices, sep=",")
    i += 1
