numeroa = int(input('Insira o primeiro número:'))
numerob = int(input('Insira o segundo número:'))
numeroc = int(input('Insira o terceiro número:'))

r = (numeroa+numerob)**2
s = (numerob+numeroc)**2
d = (r+s)/2

print(f'''
========================================
Olá, seja bem, vindo(a)!!
O resultado da equação é igual a {d:.1f}!
========================================
''')