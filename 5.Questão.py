import os

os.system("clear")

operacao = input("Digite a operação (+, -, *, /): ")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro: Divisão por zero não permitida."
else:
    resultado = "Operação inválida!"

print(f"O resultado de {A} {operacao} {B} é: {resultado}")