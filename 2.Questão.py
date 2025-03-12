import os

os.system("clear")


nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (em anos): "))
else:
    tempo_casada = None

print("\nDados do usuário:")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

if tempo_casada is not None:
    print(f"Tempo de Casada: {tempo_casada} anos")