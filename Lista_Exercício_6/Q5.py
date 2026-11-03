eleitores = int(input("Qual o número total de eleitores? "))

nulos = votos10 = votos15 = votos20 = 0

for i in range(eleitores):
    print("-------------------------------------")
    print("Candidato Paulo: número 10\n" \
    "Candidata Yasmim: número 15\n" \
    "Candidato Rogério: número 20")
    
    voto = int(input("Seu voto: "))

    if voto == 10:
        votos10 += 1
    elif voto == 15:
        votos15 += 1
    elif voto == 20:
        votos20 += 1
    else:
        nulos += 1

print(f"O Candidato Paulo recebeu {votos10} votos.\nA candidata yasmim recebeu {votos15}" \
      f" votos.\nO candidato Rogério recebeu {votos20} votos.\n{nulos} pessoa(s) votou(aram) nulo.")