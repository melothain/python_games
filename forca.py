def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.lower()
    
    letras_acertadas = ["_", "_" , "_" , "_" , "_" , "_"]

    print(letras_acertadas)

    enforcou = False
    acertou = False

    while not enforcou and not acertou: 
        chute = input('Qual letra? ')
        chute = chute.strip().lower()

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

        print("Jogando...")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()