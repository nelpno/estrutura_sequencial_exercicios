ganho_por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas_mes = float(input('Quantas horas você trabalhou esse mês? '))

salario = ganho_por_hora * horas_trabalhadas_mes

print((f'Você ganhou R$ {salario:,.2f} esse mês.'))