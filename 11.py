def prime_number(num: int):
    """
    checks that the number is prime
    :return: True if prime, False otherwise
    """
    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def all_prime():
    """
    searches for all prime numbers from 1 to n
    """
    n = int(input())
    if n < 2:
        print('нет простых чисел')
    for num in range(2, n + 1):
        if prime_number(num):
            print(num)