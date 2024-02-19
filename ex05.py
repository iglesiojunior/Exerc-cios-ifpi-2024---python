import math

valor = int(input('Insira um valor a ser decomposto e somado:'))

Centenas = valor//100
Dezenas = math.trunc((valor%100)/10)
Unidades = ((valor%100)%10)
soma = Centenas+Dezenas+Unidades

print('''
=================================
Olá!
o número {} decomposto e somado
equivale a: {}!! ({}+{}+{})
=================================
'''.format(valor, soma, Centenas, Dezenas, Unidades))

