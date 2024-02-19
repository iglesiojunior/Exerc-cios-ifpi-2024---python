numero = int(input("Digite um número de 4 dígitos:"))

milhar = numero//1000
centena = (numero%1000)//100
dezena = ((numero%1000)%100)//10
unidade = ((numero%1000)%100)%10
soma = milhar+centena+dezena+unidade

print(f'''
===============================================
Olá, seja bem vindo(a)!!
A soma dos elementos que compõem o número {numero}
({milhar} + {centena} + {dezena} + {unidade}) = {soma}
===============================================
''')