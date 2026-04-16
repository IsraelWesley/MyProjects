produto = []

valor = []

contador = 1

total = 0

maior_valor = []

total_preco = 0

mais_caro = []

while contador > 0:

    item = input("Digite o item: ")
    preco = float(input("Digite o preço do produto: "))
    total_preco += preco
    total += 1
    produto.append(item)
    valor.append(preco)
    decisao = input("Deseja continuar? (S/N): ")

    if decisao == "N" or decisao == "n":
        break



print("="*30)
print("   🛒 RESUMO DA COMPRA 🛒")
print("="*30)

for i in range(len(produto)):
    print(f"🛍️  {produto[i]} {valor[i] }R$")

print(f"\n📊 TOTAL DE ITENS: {total} Itens.")
print(f"💵 VALOR TOTAL: {total_preco} R$")
print("="*30)
print(f"💎 PRODUTOS(S) MAIS CARO(S): {max(valor)} ")
print("="*30)

dese = input("DESEJA REALIZAR UMA BUSCA? (S/N):")
if dese == "n" or dese == "N":
    while True:
        print("="*30)
        busca = input("🔎 BUSCA DE PRODUTOS: ")
        print("="*30)
       
        if busca in produto:
            print(f"📝 O produto: {busca} está no estoque")
            print("="*30)   
            break
        else:
            print("="*30)
            print("⚠️  PRODUTO NÃO ENCONTRADO NO ESTOQUE!")
            print("="*30)


















