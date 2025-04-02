Dado um array, crie uma função que retorne um novo array sem valores duplicados.

def remover_duplicados(array):
    return list(set(array))

# Exemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
array_sem_duplicados = remover_duplicados(numeros)

print(f"Array original: {numeros}")
print(f"Array sem duplicados: {array_sem_duplicados}")
