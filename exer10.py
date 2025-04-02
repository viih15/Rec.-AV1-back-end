Encontre o subarray contínuo com a maior soma dentro de um array de números inteiros

def maior_soma_subarray(array):
    maior_soma_atual = array[0]
    maior_soma_global = array[0]
    
    for i in range(1, len(array)):
        maior_soma_atual = max(array[i], maior_soma_atual + array[i])
        maior_soma_global = max(maior_soma_global, maior_soma_atual)
    
    return maior_soma_global

# Exemplo de uso
numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maior_soma = maior_soma_subarray(numeros)

print(f"A maior soma de subarray contínuo