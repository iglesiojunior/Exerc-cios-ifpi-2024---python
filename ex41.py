custofabrica = float(input('Digite o custo de fábrica do seu veículo'))

valorfinal = (custofabrica*0.45)+(custofabrica*0.28)+custofabrica

print(f'''
=====================================================
Olá, seja bem vindo(a)!
O valor de fábrica do seu veículo: R${custofabrica}
terá como valor de consumo R${valorfinal:.2f}!!
=====================================================
''')