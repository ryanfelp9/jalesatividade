import random

class RoloDeDados:
    def rolar_d6(self):
        return random.randint(1,6)
    
    def rolar_d12(self):
        return random.randint(1,12)
    
    def rolar_d20(self):
        return random.randint(1,20)
    
v=RoloDeDados()

print("o numero aleatorio é:", v.rolar_d6())
print("o numero aleatorio é:", v.rolar_d12())
print("o numero aleatorio é:", v.rolar_d20())
