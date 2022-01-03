""" Valor em Real"""
dc = float(input('How much money to you have? R$'))
""" Valor em Dolar """
us = dc / 5.47
""" Valor em Euros """
eu = dc / 6.53
print('With R${} you can by ${:.3f} and €{:.3f}'.format(dc, us, eu))