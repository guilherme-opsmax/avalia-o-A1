
print("Números pares de 1 a 100 (usando for):")

# Percorre todos os números de 1 até 100 (o 101 não é incluído)
for numero in range(1, 101):
    
    # Verifica se o número é par usando o operador módulo (%)
    # Se o resto da divisão por 2 for zero, o número é par
    if numero % 2 == 0:
        # Imprime o número par encontrado
        print(numero)
