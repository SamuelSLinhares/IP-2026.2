num = int(input("Digite um número: "))

algarismos = 0

while num >= 1.0:
    algarismos += 1
    num = num / 10

print(f"O número fornecido possui {algarismos} algarismos!")