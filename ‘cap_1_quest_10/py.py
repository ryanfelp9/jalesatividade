class ConfiguracaoJogo:
    def __init__(self, resolucao_tela, volume_audio, dificuldade):
        self.resolucao_tela = resolucao_tela
        self.volume_audio = volume_audio
        self.dificuldade = dificuldade

config = ConfiguracaoJogo("1920x1080", 75, "Fácil")

print(config.resolucao_tela)
print(config.volume_audio)
print(config.dificuldade)
