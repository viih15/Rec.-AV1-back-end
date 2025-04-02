 Dado um array de números, encontre e exiba o maior e o menor valor presentes nele.

def encontrar_maior_menor(array):
    maior = max(array)
    menor = min(array)
    return maior, menor

# Exemplo de uso
numeros = [10, 45, 2, 98, 34]
maior, menor = encontrar_maior_menor(numeros)

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")

