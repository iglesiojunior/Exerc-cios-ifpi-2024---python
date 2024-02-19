km = float(input('Insira uma velocidade em km/h:'))

conversao = km/3.6

print('''
==================================      
Olá!
A velocidade {} em km/h
equivale a {:.1f} em m/s!!
==================================      
'''.format(km, conversao))