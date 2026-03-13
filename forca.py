print("Bem vindo ao jogo de forca!!")

PalavraSecreta = "misterioso".upper()
LetrasAcertadas = ["_" for letra in PalavraSecreta]

acertou = False
enforcou = False
erros = 0

while acertou == False and enforcou == False:

    print(LetrasAcertadas)

    opcao = int(input("(1.) Digitar letra (2.) Digitar palavra "))

    if opcao == 1:

        chute = input("Digite uma letra:")
        chute = chute.strip().upper()

        
        if chute in PalavraSecreta:
            indice = 0

            for letra in PalavraSecreta:
                if chute == letra:
                    LetrasAcertadas[indice] = letra
                indice += 1
                if "_" not in LetrasAcertadas:
                    acertou = True
                    print("Você ganhou!")
                    print(LetrasAcertadas)

        else:
            erros += 1
            print("Você tem", erros, "erros")
            if erros == 6:
                enforcou = True
                print("Você perdeu! A palavra secreta era: ", PalavraSecreta)
        

    elif opcao == 2:

        chute = input("Digite a palavra: ")
        chute = chute.strip().upper()

        if chute == PalavraSecreta:
            indice = 0
            LetrasAcertadas = [PalavraSecreta[indice] for indice in range(len(PalavraSecreta))]
            acertou == True
            print("Você ganhou, a palavra está correta!!")
            print(LetrasAcertadas)
            break

        else:
            print("Você errou, a palavra secreta era: ", PalavraSecreta)
            break
        
   
