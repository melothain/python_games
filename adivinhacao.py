'''
Curso Básico Python Alura
Programa para jogo de adivinhação.
autor: thaina
criado em 29/11/2023

***********************************

Jogo de adivinhação: dado numero de tentativas e diferente niveis de dificuldades, acertar um número.
'''

import random

def jogar():
    print('**'*20)
    print('*** Bem vindo ao jogo de adivinhação ***')
    print('**'*20)

    numero_secreto = random.randrange(1,101)
    rodada = 1
    print(numero_secreto)

    dificuldade = int(input('Escolha a dificuldade do jogo: (1) Fácil; (2) Médio; (3) Difícil '))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5
    else:
        print('Digite apenas 1, 2 ou 3. ')
        

    for rodada in range(1, total_de_tentativas + 1):
        print('A rodada {} de {} começa agora:'.format(rodada, total_de_tentativas))

        chute = int(input('Digite um número entre 1 e 100: '))

        if chute < 1 or chute > 100:
            print("O número precisa ser entre 1 e 100. Tente novamente.")
            continue

        maior   = chute  > numero_secreto
        menor   = chute  < numero_secreto
        acertou = chute == numero_secreto

        if maior:
            print('Você chutou {}, que é maior que o número secreto'.format(chute))
        elif menor:
            print('Você chutou {}, que é menor que o número secreto'.format(chute))
        elif acertou:
            print('Você acertou, vyadoh!')
            break

        rodada += 1
        

if (__name__ == "__main__"):
    jogar()