from deck import Deck

game = Deck().new_game()

value1= (game[0]['cards'][0]['value'])
value2= (game[1]['cards'][0]['value'])

print(f'{value1} and {value2}')

payload = {
    "ACE": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 10,
    "QUEEN": 10,
    "KING": 10,
}

def compare_values(value):
    if value in payload:
        value_card = payload[value]
    return value_card


def verifysum(value):
    if value == 21:
        print("TWENTY ONE!")
        return value
    if value > 21:
        print(f"LOSE GAME, THE TOTAL SUM IS: {value}")
        return False
    if value < 21:
        print(f"THE CURRENT SUM IS: {value}")
        return True


'''
card1 =(compare_values(value1))

card2 =(compare_values(value2))

sum_cards = card1 + card2

response = verifysum(sum_cards)

if response == True:

'''