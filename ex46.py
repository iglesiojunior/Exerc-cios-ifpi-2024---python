quantia = float(input('Insira aqui um valor a ser parcelado:'))

prestacao = quantia//3
entrada = quantia - prestacao*2

print(f"""
====================================================
Olá, seja bem vindo!
O seu valor de {quantia} poderá ser parcelado em:
valor de entrada: {entrada:.2f}
valor de cada uma das duas(2) prestações {prestacao:.2f}
====================================================
""")
