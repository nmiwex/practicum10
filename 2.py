def fibonacci(n: int):
    """
    print n fibonacci numbers
    :param n: count of numbers
    :return: None
    """
    numbers = [1, 1]
    for i in range(2, n):
        num = numbers[i - 1] + numbers[i - 2]
        numbers.append(num)

    print(*numbers)