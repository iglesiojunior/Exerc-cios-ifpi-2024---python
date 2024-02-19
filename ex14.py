nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceita nota:'))
peso1 = int(input('Insira o primeiro peso:'))
peso2 = int(input('Insira o segundo peso:'))
peso3 = int(input('Insira o terceiro peso:'))

media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)

print (f'''
==========================
olá, espero que esteja bem!
a média das suas notas:
{nota1}, {nota2} e {nota3}
é igual a:
{media}!!!
==========================
''')