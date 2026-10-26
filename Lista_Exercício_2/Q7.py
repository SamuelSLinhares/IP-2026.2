valor = float(input("Quanto o cliente gastou em compras? "))
forma_pag = input("Qual o método de pagamento? ")

if valor >= 100 and forma_pag == "Dinheiro":
    valor_final = valor * 0.9
    print(f'Valor a ser pago: R${valor_final:.2f}')
elif forma_pag != "Dinheiro" and forma_pag != "Cheque":
    print("Forma de pagamento inválida")
else:
    print(f'Valor a ser pago: R${valor:.2f}')