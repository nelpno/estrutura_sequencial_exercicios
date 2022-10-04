ganho_por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas_mes = float(input('Quantas horas você trabalhou esse mês? '))

salario_bruto = ganho_por_hora * horas_trabalhadas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'+ Salário Bruto : R${salario_bruto:.2f}\n- IR (11%) ; R${ir:.2f}'
      f'\n- INSS (8%) : R${inss:.2f}\n- Sindicato (5%) ; R${sindicato:.2f}'
      f'\n= Salário Liquido : R${salario_liquido:.2f}')
