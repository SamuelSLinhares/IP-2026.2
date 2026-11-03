n = int(input("Digite um número: "))

if n == 0 or n == 1:
    primo = False

elif n == 2:
    primo = True

else:
    primo = True
    
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            primo = False
            break

if primo == True:
    print("É primo!")
else:
    print("Não é primo!")