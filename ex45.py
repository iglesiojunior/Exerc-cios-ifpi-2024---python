quantia = float(input('Digite a quantia desejada para saque: '))

onca = quantia//50
arara = (quantia%50)//10
garca =  ((quantia%50)%10)//5
umreal = (((quantia%50)%10)%5)

print(f'''
============================
Olá, seja bem vindo(a)!
A sua quantia de {quantia} reais terá como saque:
{onca} notas de 50
{arara} notas de 10
{garca} notas de 5
{umreal} notas de 1
===========================
''')