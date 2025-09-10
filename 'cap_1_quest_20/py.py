class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        outro.vida -= self.ataque
        if outro.vida < 0:
            outro.vida = 0
        print(f"{self.nome} ataca {outro.nome}! Vida de {outro.nome} agora é {outro.vida}.")

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque}"


class Arena:
    def iniciar_batalha(self, personagem1, personagem2):
        print(f"Batalha iniciada entre {personagem1.nome} e {personagem2.nome}!\n")
        rodada = 1
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            print(f"--- Rodada {rodada} ---")
            personagem1.atacar(personagem2)
            if not personagem2.esta_vivo():
                break
            personagem2.atacar(personagem1)
            rodada += 1
            print()
        vencedor = personagem1 if personagem1.esta_vivo() else personagem2
        print(f"\n{vencedor.nome} venceu a batalha!")


p1 = Personagem("Guerreiro", 100, 20)
p2 = Personagem("Mago", 80, 25)

print(p1)
print(p2)

arena = Arena()
arena.iniciar_batalha(p1, p2)
