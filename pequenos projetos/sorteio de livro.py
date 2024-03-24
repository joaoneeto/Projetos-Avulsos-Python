# A Vi, gosta muito de ler, mas é indecisa, então, programei um sorteio para escolher entre 3 opção de livro

from random import choice

pri = input('Digite o nome do primeiro livro: ')
seg = input('Digite o nome do segundo livro: ')
ter = input('Digite o nome do terceiro livro: ')
ale = choice([pri, seg, ter])
print(f'\nVocê ira ler essa semana: {ale}')
