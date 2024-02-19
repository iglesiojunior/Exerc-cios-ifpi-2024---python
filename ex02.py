horas = int(input('insira um valor em horas:'))
minutos = int(input('Insira um valor em minutos(se tiver, se não, coloque 0):'))

conversao = (horas*60)+minutos

print('''
=========================
O horário de {}:{} horas
equivale a: {} minutos
=========================
'''.format(horas, minutos, conversao))