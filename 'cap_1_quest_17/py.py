class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao pedido de {self.cliente}.")

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total

p1 = Produto("Notebook", 3500.00)
p2 = Produto("Mouse Gamer", 150.00)
p3 = Produto("Teclado Mecânico", 450.00)

pedido = Pedido("Ryan Felipe")

pedido.adicionar_item(p1)
pedido.adicionar_item(p2)
pedido.adicionar_item(p3)

print("\nItens do pedido:")
for item in pedido.itens:
    print(item)

print(f"\nTotal do pedido: R${pedido.calcular_total():.2f}")


