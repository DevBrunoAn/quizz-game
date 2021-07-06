
def perguntas():

    vida = True

    while (vida == True):
        print("\nDe quem é a famosa frase “Penso, logo existo”?\n")
        resposta1 = print(' a) Platão', '\n b) Galileu Galilei', '\n c) Descartes', '\n d) Sócrates', '\n e) Francis Bacon')
        userresposta1 = input("\n  Digite sua resposta: ")
        if userresposta1 == 'a':
            print('\nVocê está errado, tente novamente')
        elif userresposta1 == 'b':
            print('\nVocê está errado, tente novamente')
        elif userresposta1 == 'c':
            print('\nVocê está certo parabéns!')
            vida = False
        elif userresposta1 == 'd':
            print('\nVocê está errado, tente novamente')
        elif userresposta1 == 'e':
            print('\nVocê está errado, tente novamente')
        else:
            print('\nerro')