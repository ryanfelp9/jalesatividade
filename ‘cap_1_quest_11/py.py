class carro:
    def __init__(self):
        self.velocidade=0

    def acelerar(self, valor):
        self.velocidade+=valor

    def frear(self,valor):
        self.velocidade-=valor
        if self.velocidade<0:
            self.velocidade=0

meu_carro=carro()
meu_carro.acelerar(50)
print(meu_carro.velocidade)
meu_carro.frear(60)
print(meu_carro.velocidade)            
          
