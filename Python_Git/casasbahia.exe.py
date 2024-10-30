print("\33[31m-_-_-_-_-_ Confira as condições de pagamento _-_-_-_-_-")
produto = str(input("\33[36mDigite o tipo de produto: "))
valor = float(input(("\33[36mDigite o valor do seu produto: R$")))

forma = int(input("""\33[36mSelecione a forma de pagamento:
\33[m[1] Dinheiro
[2] Cartão
[3] Cheque
*** \33[36mDigite o número correspondente a forma de pagemento desejada: """))
while forma != 1 and forma != 2 and forma != 3:
    forma = int(input("""\33[36m\nSelecione a forma de pagamento:
\33[m[1] Dinheiro
[2] Cartão
[3] Cheque
*** Digite o número correspondente a forma de pagemento desejada: """))

if forma == 1 or forma == 3:
    print("""\33[34m\nValor pago à vista. 
    Valor final: \33[mR${:.2f}""".format(valor-(valor*0.1)))
elif forma == 2:
    parcelas = int(input("\33[36m\nDigite em quantas vezes será parcelada sua compra: "))
    if parcelas == 1:
        print("""\33[34m\nValor pago à vista. 
        Valor final: \33[mR${:.2f}""".format(valor-(valor*0.05)))
    elif parcelas == 2:
        print("""\33[36m\nParcelado em \33[31m2 vezes\33[36m de \33[mR${:.2f}.
         \33[36mValor final: \33[mR${:.2f}""".format(valor/2, valor))
    else:
        print("""\33[36m\nValor parcelado em \33[31m{} vezes\33[36m de \33[mR${:.2f}.
         \33[36mValor final: \33[mR${:.2f}""".format(parcelas, valor/parcelas, valor+(valor*0.2)))



