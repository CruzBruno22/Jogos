def Jogar_Adivinhaçao ():
        
    import time
    import random

    print ("***************************")
    print ("****JOGO DE ADIVINHAÇÃO****")
    print ('***************************')
    time.sleep (0.5)

    # Random é uma bibliteca para numeros aleatórios, (x,y) que irá do x ao y.
    secret_number = random.randrange (1,101) 
    tentativas    = 0
    pontos        = 1000

    print ("Qual nivel você quer Jogar ?")
    print ("(1) Facil (2) Médio (3) Dificil")

    nivel = int (input ("Define o Nível: "))
 
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5

    while tentativas >= 1 :
        chute = int (input ("Digite um número entre 1 e 100  "))
        tentativas = tentativas - 1
        if (chute == secret_number): # Verifica se esta Correto
            print ("Parabêns, você acertou e fez {} pontos !".format (pontos))
            break
        if (tentativas == 0):  # Verifica Mensagem final
            print("It's Enought")
            break
        if (chute > secret_number):
            print ("Você Errou. Seu chute foi Maior que o Numero Secreto.")
            print ("Você ainda tem mais {} tentativas".format(tentativas))
        if (chute < secret_number):
            print ("Você Errou. Seu chute foi Menor que o Numero Secreto.")
            print ("Você ainda tem mais {} tentativas".format(tentativas))
        pontos_perdidos = abs (secret_number - chute) # abs funçao numeros absoluto - sem o + nem -
        pontos = pontos - pontos_perdidos
    PlayAgain ()
# questionar se deseja jogar novamente
        
def PlayAgain ():
    Resposta = input("Voce Gostaria de Jogar novamente ? ")

    if (Resposta == "Sim"):
        Jogar_Adivinhaçao ()
    else:
        print("Obrigado por Jogar")
if (__name__ == __main__):
    Jogar_Adivinhaçao()
    