import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))


    palavra_secreta = palavras[numero].lower()
    
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou: 
        chute = input('Qual letra? ')
        chute = chute.strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        print("Jogando...")

    if acertou:
        print("Você ganhou! ")
    else:
        print("Você perdeu! ")   
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()