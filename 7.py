def common_multiple(a: int, b: int, n: int):
    """
    displays all common multiples of two natural numbers in ascending order
    :param a: first number
    :param b: second number
    :param n: max number
    :return: None
    """
    max_num = max(a, b)
    min_num = min(a, b)
    multiples = []

    for num in range(max_num, n + 1, max_num):
        if num % min_num == 0:
            multiples.append(num)

    print(*multiples)
