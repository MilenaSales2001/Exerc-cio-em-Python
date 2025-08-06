# criando uma fila vazia
fila = []

# adicionando elementos (enqueue)
fila.append("a")
fila.append("b")
fila.append("c")

# exibindo a fila
print("fila:", fila)  # saida: fila: ['a', 'b', 'c']

# removendo elementos (dequeue)
primeiro = fila.pop(0)
print("elemento removido:", primeiro)  # saida: elemento removido: a

# fila apos remocao
print("fila agora:", fila)  # saida: fila agora: ['b', 'c']