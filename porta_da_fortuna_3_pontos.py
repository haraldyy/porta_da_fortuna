from random import *
score=0
#essa variável guarda o número de vezes que o jogo já foi jogado
tentativas=0
#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

  ____   ____   ____
 |    | |    | |    |             
 | [1]| | [2]| | [3]|               
 |   o| |   o| |   o|         
 |    | |    | |    |        
 |____| |____| |____|
''')

#repetir, enquanto a variável 'score' seja menor que 3
while score<3:
#soma 1 ao numero de tentativas
    tentativas += 1
    
    print("\nTentativa", tentativas, ": Escolha uma porta (1, 2 ou 3):")

#pegue a porta escolhida e armazene como um número inteiro (int)
    portaescolhida = int(input())

#escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portacerta = randint(1,3)
    
#mostre ao jogador qual porta ele escolheu e qual era a porta certa
    print("A porta escolhida foi a", portaescolhida)
    print("A porta certa é a", portacerta)

#o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaescolhida==portacerta:
        print("Parabéns")
        score+= 1
    else:
        print("Que peninha!")
    print('Sua pontuação atual é',score)

print("\nVocê conseguiu! Terminou o jogo em", tentativas, "tentativas **")


