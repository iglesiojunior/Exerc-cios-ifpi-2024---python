import math

x1 = float(input('Digite o ponto x do 1º ponto:'))
y1 = float(input('Digite o ponto y do 1º ponto:'))
x2 = float(input('Digite o ponto x do 2º ponto:'))
y2 = float(input('Digite o ponto y do 2º ponto:'))

distanciadoispontos = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'''
================================
Olá, seja bem vindo(a)!
A distância entre os pontos A({x1},{y1}) e B({x2},{y2})
é igual a {distanciadoispontos:.2f}
================================
''')