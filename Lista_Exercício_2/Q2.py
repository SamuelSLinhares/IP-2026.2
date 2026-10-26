h = int(input("Qual a sua altura, em centímetros? "))

h_metros = h / 100

ideal_hom = h_metros * 72.7 - 58
ideal_mul = h_metros * 62. - 44.7

print(f'Se você for um homem, seu peso ideal é {ideal_hom:.2f}Kg')
print(f'Se você for uma mulher, seu peso ideal é {ideal_mul:.2f}Kg')