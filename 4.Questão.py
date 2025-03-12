import os

os.system("clear")



preco_morango = 7.50  # Preço por kg de morango
preco_maca = 5.00     # Preço por kg de maçã


quantidade_morangos = float(input("Digite a quantidade de morangos (em kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em kg): "))

valor_total = (quantidade_morangos * preco_morango) + (quantidade_macas * preco_maca)

quantidade_total_frutas = quantidade_morangos + quantidade_macas

if quantidade_total_frutas >= 10 or valor_total > 15.00:
    valor_total = valor_total * 0.90 

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")