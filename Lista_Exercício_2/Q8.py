valor = float(input("Quanto o cliente gastou em compras? "))
forma_pag = input("Qual o método de pagamento? ")

if forma_pag == "Cartão":
    funcao = input("Débito ou Crédito? ")

if funcao == "Crédito":
    parcelas = int(input("Quantas parcelas (max 3)? "))

if valor >= 100 and forma_pag == "Dinheiro":
    valor_final = valor * 0.9
    print(f'Valor a ser pago: R${valor_final:.2f}')
elif forma_pag == "Cartão" and funcao == "Crédito":
    valor_parcelado = valor / parcelas
    print(f'Valor Final: R${valor:.2f}')
    print(f'{parcelas} parcelas de R${valor_parcelado}')
else:
    print(f'Valor a ser pago: R${valor:.2f}')