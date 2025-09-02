class ConversorSimples:
    def real_para_dolar(self, valor_real):
        return valor_real / 5.25
    
    def dolar_para_real(self, valor_dolar):
        return valor_dolar * 5.25
    
v=ConversorSimples()

print(f"real para dolar {v.real_para_dolar(100):.2f}")
print(f"dolar para real {v.dolar_para_real(100):.2f}")

    