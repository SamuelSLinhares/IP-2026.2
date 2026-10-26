num = int(input("Digite um número: "))

maior_valor = menor_valor = num
soma_total = 0

while num != -1:
    soma_total += num

    if num > maior_valor:
        maior_valor = num

    if num < menor_valor:
        menor_valor = num
    
    num = int(input("Digite um número: "))

print(f"O menor valor fornecido foi {menor_valor}")
print(f"O maior número fornecido foi {maior_valor}")
print(f"A soma de todos os valores fornecidos é {soma_total}")