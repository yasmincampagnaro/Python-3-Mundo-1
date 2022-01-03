n1 =int(input('Digite um número:'))
""" Dobro de n """
d = n1*2
""" Triplo de n """
t = n1*3
""" Raiz quadrada de n """
r = n1 ** (1/2)

""" O resultado das variáveis ficará nos {}, na ordem que está no '.format', ou seja, {n1}, {d}, {t}, {r} """
""" '{:.2f}', indica duas casas após o ponto flutuante, ou seja, '0.00' """
print('O dobro de {} é {}. \nO triplo é {}. \nSua raiz quadrada é {:.2f}'.format(n1,d,t,r))