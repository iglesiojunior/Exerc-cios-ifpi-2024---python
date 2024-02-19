segundos = int(input('Coloque aqui uma quantidade de segundos:'))

minutos = (segundos%3600)//60
horas = segundos//3600
segundos = (segundos%3600)%60

print(f'{segundos} segundos equivale a {horas} horas, {minutos} minutos e {segundos} segundos')