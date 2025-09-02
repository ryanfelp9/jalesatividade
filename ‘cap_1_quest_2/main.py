class FormatadorDeTexto:
    def para_caixa_alta (self, letra):
        return letra.upper()

    def para_caixa_baixa (self, letra):
        return letra.lower()    
    
f=FormatadorDeTexto()

print(f.para_caixa_alta("oi"))
print(f.para_caixa_baixa("OI"))
    