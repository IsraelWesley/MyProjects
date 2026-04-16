dados = []
maiores_10 = []

for i in range(1, 6):
    num = int(input(f"Digite o {i}° valor: "))
    dados.append(num)

for numero in dados:
    if numero > 10:
        maiores_10.append(numero)

print("\nOs números maiores que 10 são: ")
for nume in maiores_10:
    print(nume)

