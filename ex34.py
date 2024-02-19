numero1 = float(input('Insira o primeiro número da sua média:'))
numero2 = float(input('Insira o segundo número da sua média:'))
numero3 = float(input('Insira o terceiro número da sua média:'))

media = (numero1+numero2+numero3)/3

print(f'''
===============================================
Olá, seja bem vindo(a)!
A média entre os números: {numero1}, {numero2} e {numero3}
é igual a: {media:.2f}
===============================================
''')