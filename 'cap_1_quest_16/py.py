
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"


class Livraria:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.titulo] = livro
        print(f"Livro {livro} adicionado ao catálogo da livraria '{self.nome}'.")

    def buscar_livro(self, titulo):
        if titulo in self.catalogo:
            return self.catalogo[titulo]
        else:
            print(f"O livro '{titulo}' não foi encontrado no catálogo.")
            return None


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("A Revolução dos Bichos", "George Orwell")

livraria = Livraria("Saber em Páginas")

livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

resultado = livraria.buscar_livro("Dom Casmurro")
if resultado:
    print("Livro encontrado:", resultado)

resultado = livraria.buscar_livro("O Senhor dos Anéis")
