num = int(input("Digite um número para exibir a tabuada: "))

print(f'Tabuada de {num}:')

for i in range(1, 11):
    res = num * i
    print(f'{num} X {i} = {res}')