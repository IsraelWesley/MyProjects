dados = []

soma_positivos = 0

negativo = []

for i in range(1, 6):

    num = int(input(f"Digite o {i}° valor: "))
    dados.append(num)

for n in dados:

    if n < 0:
        negativo.append(n)
    else:
        soma_positivos += n
        
print(f"A soma de todos os numeros positivos são: {soma_positivos} ")

