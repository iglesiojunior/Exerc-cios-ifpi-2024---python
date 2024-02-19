anos = int(input('Digite sua idade em anos:'))
meses = int(input('Digite agora sua idade em meses nesse ano:'))
dias = int(input('Digite agora sua idade em dias deste mês:'))

idade = (anos*365)+(meses*30)+(dias)#Supondo que todos os meses tem 30 dias!!

print(f'''
======================================================
Olá velhote(a), seja bem vindo(a)!!
sua idade de {anos} anos, {meses} meses e {dias} dias
equivale aproximadamente a {idade} dias de vida!!
======================================================
''')