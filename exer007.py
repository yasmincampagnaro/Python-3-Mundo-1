""" O comando 'float' indica que o resultado do input será um número flutuante, um número com vírgula """
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m1 = n1+n2
m2 = m1/2

""" '{:.1f}', indica uma casas após o ponto flutuante, ou seja, '0.0' """
print('A média do aluno é {:.1f}'.format(m2))