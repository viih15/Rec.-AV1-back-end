Dado um array de números inteiros, conte quantos são pares e quantos são ímpares

def contar_pares_impares(array):
    pares = sum(1 for num in array if num % 2 == 0)
    impares = sum(1 for num in array if num % 2 != 0)
    return pares, impares

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
pares, impares = contar_pares_impares(numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
