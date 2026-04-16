dados = []

for i in range(1, 6):
    num = int(input(f"Digite o {i}° valor: "))
    dados.append(num)

print("\nOs valores digitados foram: ", end=" ")

for numero in dados: 
    print(numero, end="  ")

print(f"\nQuantidade total de dados: {len(dados)}")