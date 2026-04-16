dados = []

pares = []

for c in range(1, 6):
    num = int(input(f"Digite o {c}° numero: "))
    dados.append(num)

for numero in dados:
    if numero % 2 == 0:
        pares.append(numero)

print("\nOs números pares são: ")
for n in pares:
    print(n)