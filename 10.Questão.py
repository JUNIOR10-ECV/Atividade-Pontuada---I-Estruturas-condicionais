import os

os.system("clear")


preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite o número de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

valor_pago = 0.0

if combustivel == 'A':  
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    
    valor_pago = litros * preco_alcool * (1 - desconto)

elif combustivel == 'G':  
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    
    valor_pago = litros * preco_gasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido!")

if valor_pago > 0:
    print(f"O valor a ser pago é R$ {valor_pago:.2f}")