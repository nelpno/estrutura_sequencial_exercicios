import math


def calculo(litro):
    # Cálculo Lata
    lata = math.ceil(litro / 18)

    # Cálculo Galão
    galao = math.ceil(litro / 3.6)

    # Cálculo Mistura Galão e Lata
    if litro / 18 >= 1:
        lata_eco = int(litro / 18)
        galao_eco = math.ceil((litro % 18) / 3.6)
    else:
        lata_eco = 0
        galao_eco = math.ceil(litro / 3.6)

    print(f'''
        Você irá utilizar {litro}L.
        Se comprar {lata} lata(s), vai gastar R${lata * 80:.2f}.
        Se comprar {galao} galão(s), vai gastar R${galao * 25:.2f}.
        Misturando você compra {lata_eco} lata(s) e {galao_eco} galões gastando R${lata_eco * 80 + galao_eco * 25:.2f}
        ''')


metros_quadrados = int(input('Quantos metros serão pintados? '))
# A cobertura é de 1 litro para cada 6 metros quadrados.
litros = math.ceil(metros_quadrados / 6 * 1.1)

calculo(litros)
