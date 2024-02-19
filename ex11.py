import math

valor = int(input('digita um número de três dígitos aí meu parceiro'))

Centenas = valor//100
Dezenas = math.trunc((valor%100)/10)
Unidades = ((valor%100)%10)
num = (Unidades*100)+(Dezenas*10)+Centenas

print(f'''
=========================
O seu número invertido é: {num}
=========================
''')