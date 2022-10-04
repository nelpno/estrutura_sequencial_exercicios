altura = float(input('Digite sua altura em m: '))
sexo = str(input('Você é homem (H) ou mulher (M)? ').upper())

if sexo == 'H':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal =  (62.1 * altura) - 44.7

print(f'Seu peso ideal é por volta de {peso_ideal:,.2f}kg.')