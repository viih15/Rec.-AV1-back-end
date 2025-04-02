Desloque todos os elementos de um array para a direita (ou esquerda).

def deslocar_esquerda(array):
    if len(array) == 0:
        return array  # Retorna o array vazio diretamente
    primeiro = array.pop(0)  # Remove o primeiro elemento
    array.append(primeiro)  # Adiciona ao final
    return array

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
array_deslocado_esquerda = deslocar_esquerda(numeros)
print(f"Array deslocado para a esquerda: {array_deslocado_esquerda}")
