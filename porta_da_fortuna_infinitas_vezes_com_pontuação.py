from random import *
#imprima as 3 portas e as instruções do jogo
score=0
jogando = True
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

#repetir, enquanto a variável 'jogando' estiver com o valor 'True' (verdadeiro)
while jogando == True:

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
        score+= 1
    else:
        print("Que peninha!")
    print('Sua pontuação é',score)
#pergunte ao jogador se ele quer jogar de novo
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input()
#termina o jogo se o jogador digita 'n'
    if resposta == 'n':
        jogando=False
print("obrigado por jogar.")
print("sua pontuação final é de", score)



  
