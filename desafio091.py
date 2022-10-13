"""Crie um programa em que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado """
from random import randint
from time import sleep

jogadores = dict(Jogador1=randint(1, 6), Jogador2=randint(1, 6), Jogador3=randint(1, 6), Jogador4=randint(1, 6))
sleep(.5)

for k, v in jogadores.items():
    print(f'{k} = {v}')
    sleep(.5)

print('-' * 15)
sleep(.5)
print('Classificando...')
sleep(.5)
print('-' * 15)

