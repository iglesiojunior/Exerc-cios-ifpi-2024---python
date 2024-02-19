dias = int(input('Digite sua idade em dias:'))

anos = (dias//365)
meses = (dias%365)//30
dias = (dias%365)%30

print(f'''
=====================================================================
Olá velhote(a), seja bem vindo(a)!!
sua idade {dias} dias
equivale aproximadamente a {anos} anos, {meses} meses e {dias} dias de vida!!
=====================================================================
''')