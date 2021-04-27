import Funcoes_EP2
import random
# Misturando baralho
baralho = Funcoes_EP2.cria_baralho()
random.shuffle(baralho)
#Colocando o baralho em ordem
i = 0
while i < len(baralho):
    print("{0}. {1}".format(i+1,baralho[i]))
    i+=1

