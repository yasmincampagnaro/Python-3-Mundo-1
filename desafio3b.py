""" O comando 'int' indica à maquina que o resultado da variável, deve ser considerado como um número inteiro """
n1= int(input('Digite um valor:'))
n2=int(input('Digite mais um:'))

""" 's' irá receber a soma dos resultados das variáveis 'n1' e 'n2' """
s=n1+n2

""" O resultado das variáveis ficará nos {}, na ordem que está no '.format', ou seja, {n1}, {n2}, {s} """
print('A soma entre {} e {} é igual {}.'.format(n1,n2,s))