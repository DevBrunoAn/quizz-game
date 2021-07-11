
def perguntas():

    vermelho = '\033[31m'
    roxo = '\033[1;94m'
    cyan = '\033[96m'
    endcolor = '\033[0m'
    verde = '\033[92m'
    azul = '\033[96m'
    fail = '\033[91m'
    bold = '\033[1m'

    vida = True
    inicio = 1

    while inicio == 1:
        chances = input('\nDigite qual será a dificudade que você quer('+cyan+'hard, medio, facil'+endcolor+'): ')
        if chances == 'hard':
            chances = 3
            inicio -= 1
        elif chances == 'medio':
            chances = 5
            inicio -= 1
        elif chances == 'facil':
            chances = 10
            inicio -= 1
        else:
            print(fail +'\nErro'+ endcolor)
             

    while (vida == True):
        print(bold, azul + "\nDe quem é a famosa frase “Penso, logo existo”?\n" + endcolor)
        resposta1 = print(' a) Platão', '\n b) Galileu Galilei', '\n c) Descartes', '\n d) Sócrates', '\n e) Francis Bacon')
        userresposta1 = input(roxo + "\n Digite sua resposta: " + endcolor)
        if userresposta1 == 'a':
            print(vermelho + '\nVocê está errado' + endcolor)
        elif userresposta1 == 'b':
            print(vermelho + '\nVocê está errado' + endcolor)
        elif userresposta1 == 'c':
            print(verde + '\nVocê está certo parabéns!\n' + endcolor)
            vida = False
            chances = 0
        elif userresposta1 == 'd':
            print(vermelho + '\nVocê está errado' + endcolor)
        elif userresposta1 == 'e':
            print(vermelho + '\nVocê está errado' + endcolor)
        else:
            print(fail + '\nErro' + endcolor)
        
        chances -= 1
        if chances == 0:
            vida = False
            print(vermelho + '\nSuas chances acabaram, tente novamente.\n' + endcolor)

        if chances > 0:   
            print('\nRestam %s vidas' %(chances))
        
        
        