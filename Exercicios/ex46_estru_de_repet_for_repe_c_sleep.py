'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA
UMA CONTAGEM REGRESSIVA PARA O ESTOURO
DE FOGOS DE ARTIFÍCIOS. INDO DE 10 A 0.
COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES'''

from time import sleep
for cont in range(10, 1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POW!')