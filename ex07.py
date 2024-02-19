num1 = float(input('Insira o 1º número a ser somado:'))
num2 = float(input('Insira o 2º número a ser somado e subtraído:'))
num3 = float(input('Insira o 3º número a ser subtraído:'))

soma = num1+num2
subtracao = num2-num3

print('''
==============================================================
Olá!!
A soma dos dois primeiros números {} e {} é igual a: {}
A subtração dos dois últimos números {} e {} é igual a: {}    
==============================================================
'''.format(num1, num2, soma, num2, num3, subtracao))