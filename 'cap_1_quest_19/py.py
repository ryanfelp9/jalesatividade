class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} | Estoque: {self.estoque}"


class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto, quantidade):
        if quantidade <= produto.estoque:
            if produto.nome in self.itens:
                self.itens[produto.nome]["quantidade"] += quantidade
            else:
                self.itens[produto.nome] = {"produto": produto, "quantidade": quantidade}
            produto.estoque -= quantidade
            print(f"{quantidade}x '{produto.nome}' adicionado ao carrinho.")
        else:
            print(f"Erro: estoque insuficiente de '{produto.nome}'. Disponível: {produto.estoque}.")

    def finalizar_compra(self):
        total = 0
        print("\nItens no carrinho:")
        for item in self.itens.values():
            produto = item["produto"]
            quantidade = item["quantidade"]
            subtotal = produto.preco * quantidade
            total += subtotal
            print(f"{quantidade}x {produto.nome} - R${subtotal:.2f}")
        print(f"\nValor total da compra: R${total:.2f}")
        return total


p1 = Produto("Notebook", 3500.00, 5)
p2 = Produto("Mouse Gamer", 150.00, 10)
p3 = Produto("Teclado Mecânico", 450.00, 2)

carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(p1, 2)
carrinho.adicionar_produto(p2, 5)
carrinho.adicionar_produto(p3, 3)
carrinho.adicionar_produto(p3, 1)

carrinho.finalizar_compra()

print("\nEstoque atualizado:")
print(p1)
print(p2)
print(p3)
