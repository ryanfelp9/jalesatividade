class GeradorDeLog:
    def infor (self, mensagem):
        return f"[INFO] - {mensagem}"
    
    def alerta (self, mensagem):
        return f"[ALERTA] - {mensagem}"
    
    def error (self, mensagem):
        return f"[ERROR] - {mensagem}"
    
l=GeradorDeLog()

print(l.infor("Sistema iniciado"))
print(l.alerta("Memória quase cheia"))
print(l.error("Falha de conexão"))

