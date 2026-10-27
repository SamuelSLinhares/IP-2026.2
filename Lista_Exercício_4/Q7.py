n_inicial = n = float(input("Qual o valor a se obter a raiz quadrada? "))
b = 2

p = (b + (n / b)) / 2

if abs(b - p) < 0.0001:
    print(p, b)
else:
    while abs(b - p) > 0.0001:
        b = p
        p = (b + (n / b)) / 2

    b = p
    print(f"A raiz quadrada de {n_inicial} é {b}")