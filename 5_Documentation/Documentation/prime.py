import sys
from math import sqrt


def prime_check(n: int) -> bool:
    """
    Check whether an integer is a prime number or not. The function goes through all odd numbers
    less than square root of the input and check if the input is divisible by that number.
    :param n: the integer if prime check
    :return: boolean
    """

    if n < 2:
        return False

    limit = int(sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False

        return True


if __name__ == '__main__':
    input_ = input('Enter a number: ')

    try:
        num = int(input_)
    except ValueError:
        print('A number was not entered.')
        sys.exit(0)

    if prime_check(num):
        print('The number is prime')
    else:
        print('The number is NOT prime')