anosfumados = int(input('Insira a quantidade de anos que você fumou:'))
cigarros = int(input('Insira a quantidade de cigarros que você fuma diariamente:'))
preço = float(input('Insira o preço da cartela de cigarro em reais:'))

gastodiario = (cigarros//20)*preço + ((cigarros%20)*preço)/20
gastoanual = (gastodiario*365)*anosfumados

print(f'''
=============================================================
Olá senhor(a) fumante!
você gastou o equivalente a R${gastoanual:.2f}!!!
Atenção, fumar faz mal a saúde, saiba os malefícios do fumo!
=============================================================
''')