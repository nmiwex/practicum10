def card_price():
    """
    calculates the value of the card based on the bonus
    :return: card price
    """
    try:
        card = int(input())
        if card == 5 or card == 10:
            return card
        if card == 25:
            return 28
        if card == 50:
            return 58
        if card == 100:
            return 120

        return 'недопустимое значение'
    except ValueError:
        print('введите число')
        return card_price()

print(card_price())