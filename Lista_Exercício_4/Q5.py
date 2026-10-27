divida = float(input("Qual o valor inicial da dívida? "))
juros_mensal = float(input("Qual o juros mensal? "))
juros = juros_mensal / 100 + 1
pag_mensal = float(input("Qual o valor da parcela mensal? "))

meses = 0

while divida > 0:
    meses += 1
    divida = divida * juros
    divida -= pag_mensal

print(f'Com um juros de {juros_mensal}%, a dívida será paga em {meses} meses')