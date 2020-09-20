from random import *
#imprima as 3 portas e as instruções do jogo
score=0
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
#Deixe o jogador fazer 3 tentativas
for tentativa in range(3):
    print("\nEscolha uma porta(1, 2 ou 3):")

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
    else:
        print("Que peninha!")




  
