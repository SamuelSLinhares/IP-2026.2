n = int(input("Qual a quantidade de elementos desejados na sequência? "))

n_ant = 1
n_ant2 = 1

for i in range(n):

    if i == 0 or i == 1:
        print(1)
        
    else:
        elemento = n_ant + n_ant2
        print(elemento)
        n_ant2 = n_ant
        n_ant = elemento
    