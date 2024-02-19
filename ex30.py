minutos = int(input('Insira aqui uma quantidade de minutos:'))

dias = minutos//1440
horas = (minutos%1440)//60
resto = (minutos%1440)%60

print(f'''
=======================================================
Olá, seja bem vindo(a)!
{minutos} minutos equivalem a {dias} dias, {horas} horas e {resto} minutos
=======================================================
''')