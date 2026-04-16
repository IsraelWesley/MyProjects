numeros = []

soma = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}° valor: "))
    numeros.append(num)

for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(f"A média de numeros é: {media}")
