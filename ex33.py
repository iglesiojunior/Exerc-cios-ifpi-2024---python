import math

valor = int(input('digita um número de três dígitos aí meu parceiro:'))

Centenas = valor//100
Dezenas = math.trunc((valor%100)/10)
Unidades = ((valor%100)%10)
inverso = (Unidades*100)+(Dezenas*10)+Centenas
soma = valor + inverso

print(f'''
==================================================================
Olá, seja bem vindo(a)!
A soma entre {valor} e seu inverso {inverso} é igual a: {soma}
==================================================================
''')