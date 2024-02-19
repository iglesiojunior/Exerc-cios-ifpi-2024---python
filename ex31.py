binario1 = int(input("Insira o primeiro dígito aqui"))
binario2 = int(input("Insira o segundo dígito aqui"))
binario3 = int(input("Insira o terceiro dígito aqui"))
binario4 = int(input("Insira o quarto dígito aqui"))

digito1 = binario1*(2**3)
digito2 = binario2*(2**2)
digito3 = binario3*(2**1)
digito4 = binario4*(2**0)
soma = digito1+digito2+digito3+digito4

print(f'''
=====================================
Olá, seja bem vindo(a)
{binario1}{binario2}{binario3}{binario4} equivale em base decimal a {soma}!!
=====================================
''')
