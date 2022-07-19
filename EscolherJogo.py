
import JogoAdivinhaçao as ja
import JogoForca

print ("***************************")
print ("*****ESCOLHA SEU JOGO******")
print ('***************************')

print (" (1) Forca (2) Adivinhaçao ")

resposta = int (input ("Qual Jogo você quer Jogar ? "))

if (resposta == 1):
    print ("Jogo da Forca")
    JogoForca.Jogar_Forca()
else:
    print("Jogo da Adivinhação")
    ja.Jogar_Adivinhaçao()

