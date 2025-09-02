class calculadora:
    def calcularareadoquadrado(self, lado):
        return lado * lado
    
    def calcularareadocirculo(self, raio):
        return 3,1415 * raio * raio
    
calc=calculadora()

print("area do quadrado é:", calc.calcularareadoquadrado(4))
print("area do quadrado é:", calc.calcularareadocirculo(3))