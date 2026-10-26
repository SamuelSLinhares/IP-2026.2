nota1 = float(input("Qual foi sua primeira nota? "))
nota2 = float(input("Qual foi sua segunda nota? "))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
elif media < 4:
    conceito = "E"

print(f"Seu conceito foi {conceito}!")