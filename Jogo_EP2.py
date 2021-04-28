print("Paciência Acordeão ")
print("================== ")
print("")
print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. ")
print("")
print("Existem apenas dois movimentos possíveis: ")
print("")
print("1. Empilhar uma carta sobre a carta imediatamente anterior; ")
print("2. Empilhar uma carta sobre a terceira carta anterior. ")
print("")
print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ")
print("")
print("1. As duas cartas possuem o mesmo valor ou ")
print("2. As duas cartas possuem o mesmo naipe. ")
print("")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ")

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
#JOGO:


pode_jogar = Funcoes_EP2.possui_movimentos_possiveis(baralho)
while pode_jogar == True:
    i = 0
    esc_carta = int(input("Escolha uma carta( digite um numero entre 1 e 52):"))
    movimentos_possiveis = Funcoes_EP2.lista_movimentos_possiveis(baralho,esc_carta-1)
    if esc_carta < 0 or esc_carta > 52:
        print("Movimento Inválido")
    elif movimentos_possiveis == []:
        print("Não há movimentos possíveis")
    elif movimentos_possiveis == [1,3]:
        opcao  = int(input("Qual opção(1 ou 3): "))
        if opcao == 1:
            baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
            while i < len(baralho):
                print("{0}. {1}".format(i+1,baralho[i]))
                i+=1
        elif opcao == 3:
            baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)
            while i < len(baralho):
                print("{0}. {1}".format(i+1,baralho[i]))
                i+=1
    elif movimentos_possiveis == [1]:
        baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
        while i < len(baralho):
                print("{0}. {1}".format(i+1,baralho[i]))
                i+=1
    elif movimentos_possiveis == [3]:
        baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)
        while i < len(baralho):
                print("{0}. {1}".format(i+1,baralho[i]))
                i+=1
# FIM DO JOGO:
while pode_jogar == False:
    if len(baralho) == 1:
        print("Parabéns! Você venceu!")
        jogar_novamente = str(input("Você quer jogar novamente? (digite sim ou não)"))
        if jogar_novamente == "sim":
            pode_jogar == True
        elif jogar_novamente == 'não':
            break
        elif jogar_novamente != 'não' or jogar_novamente != 'sim':
            print("Esta não é uma opção válida")
    elif len(baralho) > 1:
        print("Você perdeu!")
        jogar_novamente = str(input("Você quer jogar novamente? (digite sim ou não)"))
        if jogar_novamente == "sim":
            pode_jogar == True
        elif jogar_novamente == 'não':
            break
        elif jogar_novamente != 'não' or jogar_novamente != 'sim':
            print("Esta não é uma opção válida")
