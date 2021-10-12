"""Utilize este arquivo para realizar as implementações dos exercícios abaixo.
Todos foram retirados de nosso livro texto"""
import random
import string


def is_multiple(n, m):
    """R-1.1"""
    i = int(n / m)

    if (n == m * i):
        return True
    else:
        return False
    pass


def minmax(data):
    """R-1.3"""
    max_number = int(data[0])
    min_number = int(data[0])
    for i in range(len(data)):
        if (len(data) == 1):
            break
        number = data[i]
        if (max_number < int(number)):
            max_number = int(number)
            continue
        elif (int(number) < min_number):
            min_number = int(number)
            continue
    tuple_numbers = (min_number, max_number)
    print(tuple_numbers)

    pass


def squares_sum(n):
    """R-1.4"""
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print("A soma dos quadrados dos números positivos inferiories a", n, "é: ", sum_squares)

    pass


def squares_sum_2(n):
    """R-1.5"""

    sum_squares = sum([i ** 2 for i in range(n)])
    print("A soma dos quadrados dos números positivos inferiories a", n, "é: ", sum_squares)

    pass


def squares_sum_odd(n):
    """R-1.6"""

    sum_squares = 0
    for i in range(n):
        if i % 2 != 0:
            sum_squares += i ** 2
    print("A soma dos quadrados dos números positivos ímpares inferiories a", n, "é: ", sum_squares)

    pass


def squares_sum_odd_2(n):
    """R-1.7"""

    sum_squares = sum([i ** 2 for i in range(n) if i % 2 != 0])
    print("A soma dos quadrados dos números positivos inferiories a", n, "é: ", sum_squares)

    pass


def my_choice(data):
    """R-1.12"""
    random_number = random.randrange(len(data))
    result = data[random_number]
    print(result)

    pass


def distinct(data):
    """C-1.15"""
    number = 0
    numbers_equals = 0
    for i in range(len(data)):
        if (int(data[i]) != number):
            number = int(data[i])
            continue
        if (int(data[i]) == number):
            numbers_equals += 1
            continue
    if (numbers_equals > 0):
        print("Existem elementos iguais na lista")
    else:
        print("Não existem elementos iguais na lista")

    pass


def my_list():
    """C-1.18"""
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = [i * (i + 1) for i in list]
    print(new_list)

    pass


def number_of_vowels(s):
    """C-1.24"""
    vowels = 'AaEeIiOoUu'
    vowels_number = len([i for i in s if i in vowels])
    print('O número de vogais presentes no string é: ', vowels_number)

    pass


def only_words(sentence):
    """C-1.25"""
    punctuation = string.punctuation
    new_sentence = ''.join([i for i in sentence if i not in punctuation])

    print(new_sentence)

    pass


def correct_arithmetic():
    """C-1.26"""
    numbers = []
    count = 0

    for i in range(3):
        numbers.append(int(input('Digite um número:\n')))

    if (numbers[0] + numbers[1] == numbers[2]):
        count += 1

    if (numbers[1] - numbers[2] == numbers[0]):
        count += 1

    if (numbers[0] * numbers[1] == numbers[2]):
        count += 1

    if (count > 0):
        print('A sequência númerica pode ser utilizada em fórmulas aritméticas')

    pass


# Bônus
def school_pubishment():
    """P-1.34"""

    pass
