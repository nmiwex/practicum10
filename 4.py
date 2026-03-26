def make_payment(p):
    """
    check errors
    """
    if isinstance(p, (int, float)) and 20 <= p <= 1000:
        print('Успех!')
    else:
        print('Повторить попытку')