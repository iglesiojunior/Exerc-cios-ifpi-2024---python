numerador1 = int(input("Insira o primeiro numerador da 1º fração:"))
denominador1 = int(input('Insira o primeiro denominador da 1º fração:'))
numerador2 = int(input("Insira o segundo numerador da 2º fração:"))
denominador2 = int(input('Insira o segundo denominador da 2º fração:'))

denominadorfinal = denominador1*denominador2
numeradorfinal = (denominador1*numerador2)+(denominador2*numerador1)

print (f'''
=====================================
Olá!, Seja bem vindo(a)!
A soma da fração {numerador1}/{denominador1} + {numerador2}/{denominador2}
é igual a {numeradorfinal}/{denominadorfinal} 
=====================================
''')