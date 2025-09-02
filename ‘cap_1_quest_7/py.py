class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

dados = Usuario("Ryan Felipe", "ryan@gmail.com")

print(dados.nome)
print(dados.email)
