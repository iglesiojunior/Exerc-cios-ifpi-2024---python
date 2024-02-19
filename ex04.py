cotacao= float(input('Insira a cotação autal do dolar:'))
dolar = float(input('Insira um valor de dolar a ser convertido:'))

print('''
===========================================
Seja bem vindo ao conversor de dolar 1.0!!
      
O valor de ${} em dolar
equivale a:
R${:.2f} reais
      
===========================================
'''.format(dolar, dolar*cotacao))
