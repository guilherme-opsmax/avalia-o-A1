print("Números pares de 1 a 100 (usando while):")

# Variável inicial que começará a contagem
numero = 1

# Loop que continua enquanto o número for menor ou igual a 100
while numero <= 100:
    
    # Verifica se o número atual é par (resto da divisão por 2 igual a 0)
    if numero % 2 == 0:
        # Se for par, imprime o número
        print(numero)
    
    # Incrementa o valor de 'numero' a cada repetição do loop
    numero += 1
