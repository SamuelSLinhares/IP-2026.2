base = base_original = float(input("Qual a base numérica desejada? "))
expo = int(input("Qual o expoente da base? "))

###Pelas limitações de funções apresentadas pelo professor, e o uso obrigatório de for,
###a exponenciação só pode ser calculada se o expoente for igual ou maior que 0

if expo > 0:
    for i in range(expo - 1):
        base = base_original * base

else:
    base = 1

print(f"O resultado da exponenciação é: {base:.2f}")