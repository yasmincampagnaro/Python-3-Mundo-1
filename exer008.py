n1 = float(input('Uma distância em metros:'))
""" KM """
n2 = n1 / 1000 
""" Hectares """
n3 = n1 / 10000
""" Decímetro """
dec = n1 / 10
""" Centímetro """
n4 = n1 * 100
""" Milímetro """
n5 = n1 * 1000
print('A medida de {}m corresponde a: \n{} km.\n{} hec. \n{} dec. \n{} cm.\n{} mm'.format(n1, n2, n3, dec, n4, n5))

medida = float(input('Uma distância em metros:'))
km = medida / 1000
hec = medida / 10000
dec = medida / 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: \n{} km.\n{} hec. \n{} dec.\n{} cm.\n{} mm'.format(medida, km, hec, dec, cm, mm))