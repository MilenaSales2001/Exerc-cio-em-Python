# usando um dicionario para armazenar informacoes dos livros
livros = {
    'ISBN1': {'titulo': 'a arte da guerra', 'autor': 'sun tzu', 'ano': 500},
    'ISBN2': {'titulo': '1984', 'autor': 'george orwell', 'ano': 1949}
}

# definindo a classe de emprestimo
class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

# criando objetos de emprestimo
emprestimo1 = Emprestimo(livros['ISBN1'], '2023-01-01', '2023-01-15')
emprestimo2 = Emprestimo(livros['ISBN2'], '2023-02-01', '2023-02-15')

# exibindo os dados dos emprestimos
def mostrar_emprestimo(e):
    print("titulo:", e.livro['titulo'])
    print("autor:", e.livro['autor'])
    print("emprestado em:", e.data_emprestimo)
    print("devolucao prevista:", e.data_devolucao)
    print("---")

mostrar_emprestimo(emprestimo1)
mostrar_emprestimo(emprestimo2)
