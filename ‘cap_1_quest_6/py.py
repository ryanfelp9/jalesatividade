class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

dados = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

print(dados.titulo)
print(dados.autor)
print(dados.ano_publicacao)
