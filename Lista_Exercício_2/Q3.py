salario_hora = float(input("Quanto você ganha por hora trabalhada? "))
horas = int(input("Quantas horas foram trabalhadas no mês atual? "))

salario_bruto = salario_hora * horas

desconto_ir = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto_ir
desconto_inss = salario_liquido * 0.08
salario_liquido -= desconto_inss
desconto_sin = salario_liquido * 0.05
salario_liquido -= desconto_sin

print(f'Salário Bruto: R${salario_bruto:.2f}')
print(f'IR(11%): R${desconto_ir:.2f}')
print(f'INSS(8%): R${desconto_inss:.2f}')
print(f'Sindicato(5%): R${desconto_sin:.2f}')
print(f'Salário Líquido: R${salario_liquido:.2f}')