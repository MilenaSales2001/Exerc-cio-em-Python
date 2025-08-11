
class Node:
    def __init__(self, id):
        self.id = id
        self.next = None

    def __str__(self):
        return f"Processo ID: {self.id}"
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, id):
        new_node = Node(id)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if not self.head:
            return None
        removed_id = self.head.id
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return removed_id

    def peek(self):
        return self.head.id if self.head else None

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def listar_fila(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.next

process_queue = Queue()
process_queue.enqueue(101)
process_queue.enqueue(102)
process_queue.enqueue(103)

print("Fila de Processos:")
process_queue.listar_fila()

print("\n Processando demanda...")
process_id = process_queue.dequeue()
print(f"Processo {process_id} concluído.")

print("\nPróximo da fila:")
print(f"Processo {process_queue.peek()}")

print("\nFila atualizada:")
process_queue.listar_fila()
