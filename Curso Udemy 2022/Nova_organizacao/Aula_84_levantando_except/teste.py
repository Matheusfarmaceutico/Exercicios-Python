
def divide(n1, n2):
    
    if n2 == 0:
        raise ValueError("Divisão por 0 impossível")
    
    return n1 / n2
    
    

print(divide(2,0))
print("Você tentou dividir um valor por 0, tente novamente!")
print("continua")