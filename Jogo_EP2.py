print("Paciência Acordeão ")
print("================== ")
print("")
print("Seja bem-vindo(a) ao jogo de Paciência Acordeão feito por Alberto Mansur e Lior Lerner. ")
print("")
print("O seu objetivo é empilhar todas as cartas até restar apenas uma ")
print("")
print("Os movimentos possíveis são: ")
print("")
print("1. Empilhar uma carta do mesmo naípe sobre a carta imediatamente anterior.")
print("2. Empilhar uma carta do mesmo naípe sobre a terceira carta anterior. ")
print("3. Empilhar uma carta do mesmo número sobre a carta imediatamente anterior.")
print("4. Empilhar uma carta do mesmo número sobre a terceira carta anterior. ")
print("")
print("Em nosso jogo, empilhar a carta sobre uma vizinha é representada pelo número 1, e empilhar sobre a terceira carta anterior é representada pelo número 3")
print("")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ")
print("")
print('\033[1m'+"OBSERVAÇÃO: Para uma visualização melhor das cartas, é recomendado o uso do light-mode/fundo do terminal branco, por conta da cor preta presente em certos naipes." +'\033[0;0m')
print("")
print("Boa sorte!")
input("Pressione [Enter] para começar o jogo")

import Funcoes_EP2
import random
# Misturando baralho
baralho = Funcoes_EP2.cria_baralho()
random.shuffle(baralho)

#Cor do baralho:

def cor(baralho):
    i = 0
    while i < len(baralho):
        if "♣" in baralho[i]:
            print("{0}. \033[30m{1}\033[0;0m ".format(i+1,baralho[i]))
        if "♠" in baralho[i]:
            print("{0}. \033[30m{1}\033[0;0m ".format(i+1,baralho[i]))
        if "♥" in baralho[i]:
            print("{0}. \033[31m{1}\033[0;0m ".format(i+1,baralho[i]))
        if "♦" in baralho[i]:
            print("{0}. \033[31m{1}\033[0;0m ".format(i+1,baralho[i]))
        i+=1
    return ""

#JOGO:

pode_jogar = Funcoes_EP2.possui_movimentos_possiveis(baralho)
print(cor(baralho))
while pode_jogar == True:
    i = 0
    pode_jogar = Funcoes_EP2.possui_movimentos_possiveis(baralho)
    esc_carta = int(input("Escolha uma carta( digite um numero entre 1 e {0}):".format(len(baralho))))
    if esc_carta < 0 or esc_carta > 52:
        print("Movimento Inválido")
        movimentos_possiveis = Funcoes_EP2.lista_movimentos_possiveis(baralho,esc_carta-1)
    elif movimentos_possiveis == []:
        print(("Não há movimentos possíveis para a carta {0}").format(baralho[esc_carta-1]))
    elif movimentos_possiveis == [1,3]:
        opcao  = int(input("Qual opção(1 ou 3): "))
        if opcao == 1:
            baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
            print(cor(baralho))
        elif opcao == 3:
            baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)
            print(cor(baralho))
    elif movimentos_possiveis == [1]:
        baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-2)
        print(cor(baralho))
    elif movimentos_possiveis == [3]:
        baralho = Funcoes_EP2.empilha(baralho,esc_carta-1,esc_carta-4)
        print(cor(baralho))
        
# FIM DO JOGO:
while pode_jogar == False:
    if len(baralho) == 1:
        print("Parabéns! Você ganhou!")
    elif len(baralho) > 1:
        print("Você perdeu!")
