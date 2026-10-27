dividendo = num1 = float(input("Digite o dividendo: "))
divisor = num2 = float(input("Digite o divisor: "))
resultado = 0

while num1 > 0:
    num1 -= num2

    if num1 > 0:
        resultado += 1

    elif num1 == 0:
        resultado += 1
        resto = 0

    elif num1 < 0:
        resto = num1 + num2

print(f"A divisão inteira de {dividendo} por {divisor} resulta em {resultado}")
print(f'O resto da divisão é: {resto}')