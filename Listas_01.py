nomes = []

for c in range(1, 4):
    num = input(f"Digite um {c}° nome para a lista: ")
    nomes.append(num)

for nome in nomes:
    print(nome, end=" ")