# definindo a classe do no
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# funcao para percorrer a arvore em ordem
def em_ordem(no):
    if no:
        em_ordem(no.esquerda)
        print(no.valor)
        em_ordem(no.direita)

# criando os nos
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)

# exibindo os valores em ordem
em_ordem(raiz)
