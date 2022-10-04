import math

tamanho_area_pintada = float(input('Qual o tamanho da área pintada em m²? '))
quantidade_de_latas = math.ceil((tamanho_area_pintada / 3) / 18)

preco_total = quantidade_de_latas * 80.00

print(f'Você vai usar {quantidade_de_latas} lata(s) e irá gastar R${preco_total:.2f}')
