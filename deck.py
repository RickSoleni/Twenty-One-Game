import requests

deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

response = deck.json()

twentyonedeck = response["deck_id"]

def new_game(deck_id):
    shuffle = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
    draw1card = requests.get(
        f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
    )
    card = draw1card.json()
    return [card["cards"][0]["value"], card["cards"][1]["value"]]

def draw_one_card(deck_id):
    draw1card = requests.get(
        f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
    )
    card = draw1card.json()
    return card["cards"][0]["value"]

cards = new_game(twentyonedeck)

new_card = draw_one_card(twentyonedeck)