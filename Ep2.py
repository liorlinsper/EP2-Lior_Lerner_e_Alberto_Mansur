#Lista de cartas:
def cria_baralho():
    lista_de_cartas = ['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♠','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♥','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦']
    return lista_de_cartas

#Extração de Naipe:
def extrai_naipe(carta):
    if "♠" in carta:
        return "♠"
    elif "♥" in carta:
        return "♥"
    elif "♣" in carta:
        return "♣"
    elif "♦" in carta:
        return "♦"
    
#Extração de valores:
def extrai_valor(carta):
    if "A" in carta:
        return "A"
    elif "2" in carta:
        return "2"
    elif "3" in carta:
        return "3"
    elif "4" in carta:
        return "4"
    elif "5" in carta:
        return "5"
    elif "6" in carta:
        return "6"
    elif "7" in carta:
        return "7"
    elif "8" in carta:
        return "8"
    elif "9" in carta:
        return "9"
    elif "10" in carta:
        return "10"
    elif "J" in carta:
        return "J"
    elif "Q" in carta:
        return "Q"
    elif "K" in carta:
        return "K"

    # Movimentos possíveis para as cartas:
    
def lista_movimentos_possiveis(baralho,posicao):
    movimentos_gerais = [0]*len(baralho)
    #Caso o índice seja = 0
    if posicao == 0:
        return []
    #Outros índices:
    i = 0
    while i < len(baralho):
        #NAIPE:

        #Caso a carta possa realizar qualquer movimento: 
        if (baralho[i-1][0] == baralho[i][0]) and (baralho[i-3][0] == baralho[i][0]):
            movimentos_gerais[i] = [1,3]
        #Caso a carta possa  ser apenas empilhada:
        elif baralho[i-1][0] == baralho[i][0]:
            movimentos_gerais[i] = [1]
        #Caso a carta possa ser emplihada apenas sobre o terceiro vizinho anterior:
        elif baralho[i-3][0] == baralho[i][0]:
            movimentos_gerais[i] = [3]
        
        #LETRA:

         #Caso a carta possa realizar qualquer movimento: 
        if (baralho[i-1][1] == baralho[i][1]) and (baralho[i-3][1] == baralho[i][1]):
            movimentos_gerais[i] = [1,3]
        #Caso a carta possa  ser apenas empilhada:
        elif baralho[i-1][1] == baralho[i][1]:
            movimentos_gerais[i] = [1]
        #Caso a carta possa ser emplihada apenas sobre o terceiro vizinho anterior:
        elif baralho[i-3][1] == baralho[i][1]:
            movimentos_gerais[i] = [3]
        #Nenhum movimento possível para a carta:
        else:
            movimentos_gerais[i] = []
        i += 1
    
    return (movimentos_gerais[posicao])
