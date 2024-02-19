a = float(input('Digite o valor de a da equação: '))
b = float(input('Digite o valor de b da equação: '))
c = float(input('Digite o valor de c da equação: '))
d = float(input('Digite o valor de d da equação: '))
e = float(input('Digite o valor de e da equação: '))
f = float(input('Digite o valor de f da equação: '))

x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)

print(f'''
======================================
Olá, seja bem vindo(a)!
O resultado da equação:
{a}x + {b}y = {c}
{d}x + {e}y = {f}
é igual a:
x = {x}
y = {y}
======================================
''')