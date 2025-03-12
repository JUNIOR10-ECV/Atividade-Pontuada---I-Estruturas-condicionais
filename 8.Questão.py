import os

os.system("clear")

precos = {
    "vermelho": 25.00,
    "azul": 30.00,
    "verde": 35.00,
    "amarelo": 40.00
}

cor = input("Digite a cor do CD (vermelho, azul, verde, amarelo): ").strip().lower()

if cor in precos:
    print(f"O preço do CD {cor} é R$ {precos[cor]:.2f}")
else:
    print("Cor inválida! Por favor, escolha uma cor válida (vermelho, azul, verde, amarelo).")