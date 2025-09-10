class Disciplina:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Disciplina: {self.nome}"


class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas_lecionadas = []

    def lecionar_disciplina(self, disciplina):
        self.disciplinas_lecionadas.append(disciplina)
        print(f"O professor {self.nome} agora leciona {disciplina.nome}.")

    def __str__(self):
        disciplinas = ", ".join(d.nome for d in self.disciplinas_lecionadas) if self.disciplinas_lecionadas else "Nenhuma"
        return f"Professor: {self.nome} | Disciplinas: {disciplinas}"


d1 = Disciplina("Matemática")
d2 = Disciplina("Física")
d3 = Disciplina("História")

prof1 = Professor("João")
prof2 = Professor("Maria")

prof1.lecionar_disciplina(d1)
prof1.lecionar_disciplina(d2)
prof2.lecionar_disciplina(d3)

print("\nLista de professores e suas disciplinas:")
print(prof1)
print(prof2)
