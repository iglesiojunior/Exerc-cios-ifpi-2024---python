meses = int(input('Insira uma quantidade de meses aqui:'))

anos = meses//12
resto = meses%12

print(f'''
=============================================
Olá, seja bem vindo(a)
{meses} meses correspondem a {anos} anos e {resto} meses!!
=============================================
''')