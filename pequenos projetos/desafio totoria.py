# DESAFIO DE ESCREVER NOME DELA SO ÁS 2 PRIMEIRA LETRA DE CADA PALAVRA

nome = 'Vitoria Manuely Rodrigues'
divido = nome.split()
n1 = divido[0][0:2]
n2 = divido[1][0:2]
n3 = divido[2][0:2]
resultado = n1 + n2 +n3
print(resultado.upper())