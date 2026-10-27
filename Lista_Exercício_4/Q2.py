num = float(input("Digite um valor: "))

menor_valor = maior_valor = num
soma_total = 0

while num != -1:

    if num < menor_valor:
        menor_valor = num

    if num > maior_valor:
        maior_valor = num

    soma_total += num

    num = float(input("Digite um valor: "))

print(f"O menor valor digitado foi {menor_valor}")
print(f"O maior valor digitado foi {maior_valor}")
print(f"A soma de todos os valores é {soma_total}")