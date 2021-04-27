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

#JOGO:

i = 0
while i < len(baralho):
    print("{0}. {1}".format(i+1,baralho[i]))
    i+=1

baralho1 = baralho
pode_jogar = Funcoes_EP2.possui_movimentos_possiveis(baralho)
while pode_jogar == True:
    i = 0
    while i < len(baralho):
        print("{0}. {1}".format(i+1,baralho[i]))
        i+=1
    esc_carta = int(input("Escolha uma carta( digite um numero entre 1 e 52):"))
    movimentos_possiveis = Funcoes_EP2.lista_movimentos_possiveis(baralho,esc_carta)
    if esc_carta < 0 or esc_carta > 52:
        print("Movimento Inválido")
    elif movimentos_possiveis == []:
        print("Não há movimentos possíveis")
    elif movimentos_possiveis == [1,3]:
        opcao  = int(input("Qual opção(1 ou 3): "))
        if opcao == 1:
            baralho1 = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
        elif opcao == 3:
            baralho1 = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)
    elif movimentos_possiveis == [1]:
        baralho1 = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
    elif movimentos_possiveis == [3]:
        baralho1 = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)

    print(baralho1)
