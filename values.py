from deck import cards, new_card

print(cards)

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
    "RANDOM": 11
}


def compare_values(value):
    if value in payload:
        value_card = payload[value]
    return value_card


def sum_values(card1, card2):
    value1 = compare_values(card1)
    value2 = compare_values(card2)
    return value1 + value2


def one_more_card(value):
    newcard = compare_values(value)
    return newcard


def verifysum(value):
    if value == 21:
        return "TWENTY ONE!"
    if value > 21:
        return f"LOSE GAME: {value}"
    while value < 21:
        newcard = continuegame()
        print(f"You drawed a: {newcard}")
        newvalue = value + newcard
        print(f"Total Sum: {newvalue}")


def continuegame():
    response = input("You want draw a new card? Type Y or N: ")
    if response == "Y" or "y":
        card = one_more_card(new_card)
        return card


def game(value1, value2):
    total_sum = sum_values(value1, value2)
    verifysum(total_sum)


game(cards[0], cards[1])


# resultado
