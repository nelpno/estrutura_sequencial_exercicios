# peso máximo por peixe 50kg, excedente R$4,00/kg

peso_peixes = float(input('Quantos kg de peixe você pescou hoje? '))

excesso_de_peso = peso_peixes - 50

if excesso_de_peso > 0:
    multa = excesso_de_peso * 4
    print(f'Você vai pagar de multa R${multa:.2f}.')
else:
    print('Você não passou do limite de peso.')