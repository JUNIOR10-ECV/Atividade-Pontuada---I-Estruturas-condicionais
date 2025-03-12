import os

os.system("clear")

renda_mensal = float(input("Digite a sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
numero_prestacoes = int(input("Digite o número de prestações desejadas: "))

prestacao_mensal = valor_emprestimo / numero_prestacoes

limite_emprestimo = renda_mensal * 10

limite_prestacao = renda_mensal * 0.30

if valor_emprestimo <= limite_emprestimo and prestacao_mensal <= limite_prestacao:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido.")