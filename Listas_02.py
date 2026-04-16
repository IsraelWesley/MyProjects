numeros = []

for c in range(1, 5):
    num  = int(input(f"Digite um {c}°numero para a lista: "))
    numeros.append(num)

for numero in numeros:
    print(numero, end=" ")
