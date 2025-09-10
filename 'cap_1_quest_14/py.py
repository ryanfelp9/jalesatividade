class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        outro.receber_dano(self.ataque)
        print(f"{self.nome} atacou {outro.nome} causando {self.ataque} de dano!")

    def receber_dano(self, valor):
        self.vida -= valor
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {valor} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0


p1 = Personagem("Herói", 100, 20)
p2 = Personagem("Monstro", 80, 15)

p1.atacar(p2)
p2.atacar(p1)
p1.atacar(p2)
p1.atacar(p2)
