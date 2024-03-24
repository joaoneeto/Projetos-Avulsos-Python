# A Vi, normalmente em 1h de leitura ler 26 paginas e quer saber quanto tempo termina um livro

# saber quantas paginas tem um livro
# dividir essas paginas por horas
# distribuir ás horas por tantos dias que ela quer ler

pagina = int(input('Digite a quantidade de paginas que tem no livro: '))
horas = pagina / 26
minutos = (pagina % 26) / 60
print('Você tera quer {:.0f}Horas e {}Minutos'.format(horas, minutos))






