
class Prontuario:
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    def __str__(self):
        return f"Paciente: {self.paciente}\nDiagnóstico: {self.diagnostico}\nTratamento: {self.tratamento}"
class ListaEncadeadaProntuarios:
    def __init__(self):
        self.cabeca = None

    def adicionar_prontuario(self, paciente, diagnostico, tratamento):
        novo_prontuario = Prontuario(paciente, diagnostico, tratamento, self.cabeca)
        self.cabeca = novo_prontuario

    def buscar_prontuario(self, nome_paciente):
        atual = self.cabeca
        while atual:
            if atual.paciente == nome_paciente:
                return atual
            atual = atual.proximo
        return None

    def remover_prontuario(self, nome_paciente):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.paciente == nome_paciente:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar_prontuarios(self):
        atual = self.cabeca
        while atual:
            print(atual)
            print("-" * 30)
            atual = atual.proximo

sistema_prontuarios = ListaEncadeadaProntuarios()
sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes Tipo 2", "Metformina")
sistema_prontuarios.adicionar_prontuario("João Silva", "Hipertensão", "Losartana")
sistema_prontuarios.adicionar_prontuario("Carlos Lima", "Asma", "Salbutamol")

print("Lista de Prontuários:")
sistema_prontuarios.listar_prontuarios()

print("\nBuscando prontuário de Alice Santos:")
prontuario = sistema_prontuarios.buscar_prontuario("Alice Santos")
if prontuario:
    print(prontuario)
else:
    print("Prontuário não encontrado.")

print("\n Removendo prontuário de João Silva...")
if sistema_prontuarios.remover_prontuario("João Silva"):
    print("Prontuário removido com sucesso.")
else:
    print("Prontuário não encontrado.")

print("\n 'Lista atualizada de Prontuários:")
sistema_prontuarios.listar_prontuarios()
