class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

item = Produto("Camiseta", 49.90, 100)

print(item.nome)
print(item.preco)
print(item.estoque)
