# definindo o grafo
grafo = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["b", "c"]
}

# funcao para exibir as conexoes
def mostrar_grafo(g):
    for vertice in g:
        print(vertice, "->", g[vertice])

# exibindo o grafo
mostrar_grafo(grafo)
