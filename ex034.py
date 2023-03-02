sal = float(input('Digite o seu salário: R$'))
if sal >= 1250:
    aum = sal * 0.10
    saln = aum + sal
    print('O seu salário de R${} obteve um aumento de 10% (R${:.2f}) obtendo o valor final de R${}.'.format(sal, aum, saln))
else:
    aum = sal * 0.15
    saln = aum + sal
    print('O seu salário de R${} obteve um aumento de 15% (R${:.2f}) obtendo o valor final de R${}.'.format(sal, aum, saln))
