# Crio uma lista para ser preenchida
listanum = []
# Crio um acumulador
mai = 0 
# Crio outro acumulador
men = 0
# Crio um laço para repetir 5 vezes o programa
for c in range(0, 5):
    # A cada valor digitado é acrescentado a lista
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    # Se a primeira vez estiver em 0:
    if c == 0:
        # O menor vai receber a lista e o maior vai receber o numero do acumulador menor
        mai = men = listanum[c]
    # Senão
    else:
        # Se o numero atual digitado da lista for maior que o acumulador maior:
        if listanum[c] > mai:
            # Esse valor vai substituir o ultimo valor e vai para o acumulador 
            mai = listanum[c]
        # Se o numero atual digitado da lista for menor que o acumulador menor:
        if listanum[c] < men:
            # Esse valor vai substituir o ultimo valor e vai para o acumulador
            men = listanum[c]
# Imprimir design
print('-=+'*30)
# Imprimir formatado os valores digitados para a lista
print(f'Voce digitou os valores {listanum}')
# Imprimir o maior valor formatado para a lista usando o acumulador maior
print(f'O maior valor digitado foi {mai} nas posições', end=" ")
# para o indice e o valor numere
for i, v in enumerate(listanum):

    if v == mai:

        print(f"{i}...", end=" ")

print()

print(f"O menor valor digitado foi {men} nas posicoes ", end=" ")

for i, v in enumerate(listanum):

    if v  == men:

        print(f'O menor valor digitado foi {men} nas posições ', end=" ")

print()



    

