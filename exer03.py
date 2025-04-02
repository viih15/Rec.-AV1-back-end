Receba um array de números e calcule a média aritmética dos valores.

def calcular_media(array):
    if len(array) == 0:
        return 0  # Evita divisão por zero no caso de um array vazio
    return sum(array) / len(array)

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)

print(f"A média aritmética é: {media}")
