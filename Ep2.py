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
