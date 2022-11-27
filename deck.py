import requests


class Deck:
    def __init__(self):
        deck = requests.get(
            "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        )
        self.deck = deck.json()
        self.deck_id = self.deck["deck_id"]

    def draw_card(self) -> dict:
        requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle/")
        response = requests.get(
            f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1"
        )
        card = response.json()
        return card

    def new_game(self) -> list:
        card1 = self.draw_card()
        card2 = self.draw_card()

        return [card1, card2]


# 1- Criar novo deck.
# 2- Pega duas cartas para o player:
#   2.1 - Shuffle no deck
#   2.2 - Pegar duas cartas
# 3- Somar o valor das cartas
# 4- Perguntar para o player se ele deseja uma nova carta
# 5- Caso deseje, puxar mais uma carta, adicionar às cartas do player
# 5.1- Caso o valor esteja abaixo de 21, perguntar se ainda quer carta
# 5.2- Caso seja 21, ele ganhou
# 5.3- Caso passe de 21, ele perdeu
# 5.4- Caso ele não deseje mais cartas, pegue cartas para o crupiê
