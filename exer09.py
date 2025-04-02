Dado dois arrays, retorne um novo array contendo apenas os elementos presentes em ambos (interseção).

def interseccao_arrays(array1, array2):
    return list(set(array1) & set(array2))

# Exemplo de uso
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
resultado = interseccao_arrays(array1, array2)

print(f"Interseção dos arrays: {resultado}")

