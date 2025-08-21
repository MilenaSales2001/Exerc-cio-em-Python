class PedidoGas:
    def __init__(self, nome, endereco, tipo, pagamento):
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
        self.pagamento = pagamento
        self.status = "Recebido"

    def verificar_estoque(self, estoque):
        if estoque.get(self.tipo, 0) > 0:
            self.status = "Confirmado"
            estoque[self.tipo] -= 1
        else:
            self.status = "Indisponível"

    def preparar_entrega(self):
        if self.status == "Confirmado":
            self.status = "Em rota"

    def concluir_entrega(self):
        if self.status == "Em rota":
            self.status = "Entregue"

# Exemplo de uso
estoque = {'P13': 10, 'P45': 5}
pedido = PedidoGas("Milena", "Rua das Palmeiras, 123", "P13", "Pix")

pedido.verificar_estoque(estoque)
pedido.preparar_entrega()
pedido.concluir_entrega()

print(f"Status do pedido: {pedido.status}")
