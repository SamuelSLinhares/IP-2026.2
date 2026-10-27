continuar = True
total_compras = 0


while continuar:
    print("Produtos Disponíveis")
    print("-----------------------")
    print("(1) A\n" 
    "(2) B\n" 
    "(3) C\n" 
    "(4) D\n" 
    "(5) E\n" \
    "(0) Finalizar Compra")

    escolha = int(input("Qual produto você deseja comprar? "))

    if escolha == 1:
        qtd = int(input("Qual a quantidade desejada desse produto? "))
        total_compras += 5.50 * qtd
        print("Operação Finalizada!")
    elif escolha == 2:
        total_compras += 2.30 * qtd
        qtd = int(input("Qual a quantidade desejada desse produto? "))
        print("Operação Finalizada!")
    elif escolha == 3:
        qtd = int(input("Qual a quantidade desejada desse produto? "))
        total_compras += 4.75 * qtd
        print("Operação Finalizada!")
    elif escolha == 4:
        qtd = int(input("Qual a quantidade desejada desse produto? "))
        total_compras += 6.80 * qtd
        print("Operação Finalizada!")
    elif escolha == 5:
        qtd = int(input("Qual a quantidade desejada desse produto? "))
        total_compras += 9.30 * qtd
        print("Operação Finalizada!")
    elif escolha == 0:
        print(f"O total de suas compras resultou em R${total_compras:.2f}")
    else:
        print("Código inválido. Tente novamente!")