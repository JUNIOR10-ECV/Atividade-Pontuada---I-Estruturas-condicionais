import os

os.system("clear")

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02  # 2% de desconto
elif quantidade <= 10:
    desconto = total * 0.03  # 3% de desconto
else:
    desconto = total * 0.05  # 5% de desconto

total_a_pagar = total - desconto

print(f"\nProduto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total (sem desconto): R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")