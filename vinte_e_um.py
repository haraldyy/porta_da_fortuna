#importa a função random
from random import *
score=0
#imprime as regras do jogo
print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')
#repetir enquanto a variável 'score' for menor que 21
while score<21:
#armazena o proximo número aleatorio na variável 'prox' e adicona no 'score'
    prox=randint(1,10)
    score+= prox
#imprime o próximo número e a pontuação
    print(f'Seu próximo número é {prox}')
    print(f'sua pontuação agora é {score}')
#pergunta ao jogador se ele quer adicionar outro número
    jogo=str(input('\nGostaria de somar mais um número (s/n)\n'))
    if jogo == 's':continue
    else:
        print(f'Sua pontuação final é {score}')
        break
#o jogador ganha se a variável 'score' for igual a 21
if score ==21:
    print('VOCÊ VENCEU!!')
else:
    print('Que peninha')
