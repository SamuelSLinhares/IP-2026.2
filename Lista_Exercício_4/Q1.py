cont = 1
soma_total = 0

while cont <= 500:
    if (cont % 2 == 1) and (cont % 3 == 0):
        soma_total += cont
    cont += 1

print(f"A soma total dos números que se encaixam nos requisitos é {soma_total}")