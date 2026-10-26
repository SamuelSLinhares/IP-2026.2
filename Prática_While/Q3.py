senha = input("Digite a senha desejada: ")

tentativas_incorretas = 0

while tentativas_incorretas < 3:
    tentativa = input("Digite sua senha: ")

    if tentativa != senha and tentativas_incorretas < 3:
        print("Senha incorreta. Digite Novamente")
        tentativas_incorretas += 1

    else:
        print("Login realizado com sucesso!")
        break

    if tentativas_incorretas == 3:
        print("Senha bloqueada")