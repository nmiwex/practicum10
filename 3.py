def discounted_price(cost: float, card: bool, holiday: bool):
    """
    calculates the final discount
    """
    total_discount = 0
    if holiday:
        total_discount += 3
    if card:
        total_discount += 5

    if cost > 30000:
        total_discount += 10
    elif cost > 20000:
        total_discount += 7
    elif cost > 15000:
        total_discount += 5
    elif cost > 5000:
        total_discount += 3

    if total_discount < 15:
        total_discount = 15

    return round(cost * (1 - total_discount / 100), 2)