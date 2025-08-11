
livros = {
    'ISBN1': {'título': 'A Arte da Guerra', 'autor': 'Sun Tzu', 'ano': 500},
    'ISBN2': {'título': '1984', 'autor': 'George Orwell', 'ano': 1949},
    'ISBN3': {'título': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': 1899}
}
from datetime import datetime

class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.data_emprestimo = datetime.strptime(data_emprestimo, '%Y-%m-%d')
        self.data_devolucao = datetime.strptime(data_devolucao, '%Y-%m-%d')
        self.data_entrega_real = None

    def registrar_entrega(self, data_entrega_real):
        self.data_entrega_real = datetime.strptime(data_entrega_real, '%Y-%m-%d')

    def calcular_atraso(self):
        if not self.data_entrega_real:
            return "Livro ainda não devolvido."
        atraso = (self.data_entrega_real - self.data_devolucao).days
        return atraso if atraso > 0 else 0

    def calcular_multa(self, valor_por_dia=2.0):
        atraso = self.calcular_atraso()
        if isinstance(atraso, int) and atraso > 0:
            return atraso * valor_por_dia
        return 0.0

emprestimo1 = Emprestimo(livros['ISBN1'], '2025-08-01', '2025-08-10')
emprestimo1.registrar_entrega('2025-08-15')

print(f"Atraso: {emprestimo1.calcular_atraso()} dias")
print(f"Multa: R${emprestimo1.calcular_multa():.2f}")
