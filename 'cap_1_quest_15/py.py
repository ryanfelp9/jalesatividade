class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"Música '{musica}' adicionada à playlist '{self.nome}'.")

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"Música '{musica}' removida da playlist '{self.nome}'.")
        else:
            print(f"Música '{musica}' não encontrada na playlist '{self.nome}'.")

    def listar_musicas(self):
        if not self.musicas:
            print(f"A playlist '{self.nome}' está vazia.")
        else:
            print(f"Playlist '{self.nome}':")
            for i, musica in enumerate(self.musicas, start=1):
                print(f"{i}. {musica}")


p = Playlist("Treino")

p.adicionar_musica("Thunderstruck - AC/DC")
p.adicionar_musica("Lose Yourself - Eminem")
p.adicionar_musica("Shape of You - Ed Sheeran")

p.listar_musicas()

p.remover_musica("Lose Yourself - Eminem")
p.listar_musicas()
