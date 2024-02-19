horas = int(input('Insira uma quantidade de horas aqui:'))

semanas = horas//168
dias = (horas%168)//24
resto = (horas%168)%24

print(f'''
====================================================================
Olá, seja bem vindo!
{horas} horas equivalem a {semanas} semanas, {dias} dias e {resto} horas!
====================================================================
''')

