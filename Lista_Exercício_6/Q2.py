dep_inicial = float(input("Qual o valor do depósito inicial, em reais? "))
juros = float(input("Qual a taxa de juros, em decimal? "))
juros = juros / 100 + 1

lucro = 0

for i in range(24):
    valor = dep_inicial * juros
    print(f'Mẽs {i + 1}: R${valor}')
    lucro += valor - dep_inicial
    dep_inicial = valor

print(f'O lucro, em 24 meses, foi de R${lucro:.2f}')