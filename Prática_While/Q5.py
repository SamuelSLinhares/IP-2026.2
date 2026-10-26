rodar = True
saldo = 0.00

while rodar:
    print("<1> Depositar\n"
    "<2> Sacar\n"
    "<3> Consultar Saldo\n"
    "<4> Sair")

    escolha = int(input("O que você deseja fazer? "))

    if escolha == 1:
        dinheiro = float(input("Qual o valor a ser depositado? R$"))
        saldo += dinheiro
        print("Operação realizada com sucesso!")

    elif escolha == 2:
        dinheiro = float(input("Qual valor a ser sacado? R$"))
        if dinheiro > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= dinheiro
            print("Operação realizada com sucesso!")

    elif escolha == 3:
        print(f"Seu saldo é R${saldo:.2f}")

    elif escolha == 4:
        rodar = False

    else:
        print("Opção inválida! Tente novamente.")