numeros = []

soma = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}° valor: "))
    numeros.append(num)

for numero in numeros:
    soma += numero

print(f"Quantidade total de numeros somados: {soma}")

