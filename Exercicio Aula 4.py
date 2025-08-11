# 5 filas, 10 colunas
assentos = [[0 for _ in range(10)] for _ in range(5)]  # 0 = disponível, 1 = reservado

def mostrar_assentos():
    print("Mapa de Assentos (0 = livre, 1 = reservado):")
    for i, fila in enumerate(assentos):
        print(f"Fila {i+1}: {fila}")
from collections import deque

fila_reservas = deque()

def adicionar_reserva(nome_cliente, fila, coluna):
    fila_reservas.append((nome_cliente, fila, coluna))
    print(f"Solicitação adicionada: {nome_cliente} deseja reservar assento [{fila+1}, {coluna+1}]")

def processar_reserva():
    if not fila_reservas:
        print("Nenhuma reserva pendente.")
        return
    nome, f, c = fila_reservas.popleft()
    if assentos[f][c] == 0:
        assentos[f][c] = 1
        print(f"Reserva confirmada para {nome} no assento [{f+1}, {c+1}]")
    else:
        print(f"Assento [{f+1}, {c+1}] já está ocupado. Reserva de {nome} não concluída.")

class NodoAssento:
    def __init__(self, fila, coluna, distancia_tela):
        self.fila = fila
        self.coluna = coluna
        self.distancia_tela = distancia_tela
        self.esquerda = None
        self.direita = None

def inserir_nodo(raiz, novo):
    if not raiz:
        return novo
    if novo.distancia_tela < raiz.distancia_tela:
        raiz.esquerda = inserir_nodo(raiz.esquerda, novo)
    else:
        raiz.direita = inserir_nodo(raiz.direita, novo)
    return raiz

def buscar_assento_por_distancia(raiz, preferencia):
    if not raiz:
        return None
    if raiz.distancia_tela == preferencia and assentos[raiz.fila][raiz.coluna] == 0:
        return raiz
    elif preferencia < raiz.distancia_tela:
        return buscar_assento_por_distancia(raiz.esquerda, preferencia)
    else:
        return buscar_assento_por_distancia(raiz.direita, preferencia)

# Mostrar assentos
mostrar_assentos()

# Adicionar reservas
adicionar_reserva("Milena", 0, 2)
adicionar_reserva("Carlos", 1, 5)

# Processar reservas
processar_reserva()
processar_reserva()

# Construir árvore de assentos com distância da tela (fila 0 = mais próxima)
raiz = None
for f in range(5):
    for c in range(10):
        nodo = NodoAssento(f, c, f)  # distância = número da fila
        raiz = inserir_nodo(raiz, nodo)

# Buscar assento com preferência de distância
preferido = buscar_assento_por_distancia(raiz, 2)
if preferido:
    print(f"Assento sugerido: Fila {preferido.fila+1}, Coluna {preferido.coluna+1}")
else:
    print("Nenhum assento disponível com essa preferência.")
