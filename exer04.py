Escreva um programa que inverta a ordem dos elementos de um array.

def inverter_array(array):
    return array[::-1]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
array_invertido = inverter_array(numeros)

print(f"Array original: {numeros}")
print(f"Array invertido: {array_invertido}")

