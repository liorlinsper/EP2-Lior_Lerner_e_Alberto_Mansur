#Lista de cartas:
def cria_baralho():
    lista_de_cartas = ['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♠','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♥','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦']
    return lista_de_cartas

def extrai_naipe(carta):
    if "♠" in carta:
        return "♠"
    elif "♥" in carta:
        return "♥"
    elif "♣" in carta:
        return "♣"
    elif "♦" in carta:
        return "♦"
