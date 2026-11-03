n = int(input("Quantas pessoas existem na turma? "))

soma_idades = 0

for i in range(n):
    idade = int(input(f"Qual a idade do aluno {i + 1}? "))
    soma_idades += idade

media = soma_idades / n

if media <= 25:
    print("A turma é jovem!")
elif media > 25 and media <= 60:
    print("A turma é adulta!")
else:
    print("A turma é idosa!")