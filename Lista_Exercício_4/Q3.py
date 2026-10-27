pop_x = 70000
pop_y = 180000
anos = 0

while pop_x < pop_y:
    anos += 1

    pop_x = pop_x * 1.035
    pop_y = pop_y * 1.015

print(f"O país X precisa de {anos} anos para ultrapassar a população do país y")