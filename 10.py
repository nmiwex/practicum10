def allowed_numbers(a: int, b: int):
    """
    check that the number consists of allowed digits
    """
    if a > b:
        a, b = b, a
    allowed_digits = {'1', '3', '4', '8', '9'}
    is_allowed = False

    for number in range(a, b + 1):
        num_str = str(number)
        if set(num_str).issubset(allowed_digits):
            print(number)
            is_allowed = True

    if not is_allowed:
        print('В диапазоне нет подходящих чисел')