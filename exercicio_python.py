"""Utilize este arquivo para realizar as implementações dos exercícios abaixo.
Todos foram retirados de nosso livro texto"""


def is_multiple(n, m):
    """R-1.1"""
    i = int(n / m)

    if(n == m * i):
        return True
    else:
        return False
    pass

def minmax(data):
    """R-1.3"""
    max_number = int(data[0])
    min_number = int(data[0])
    for i in range(len(data)):
        if(len(data) == 1):
            break
        number = data[i]
        if(max_number < int(number)):
            max_number = int(number)
            continue
        elif(int(number) < min_number):
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

    print("A soma dos quadrados dos números positivos inferiories a",n,"é: ",sum_squares)

    pass


def squares_sum_2(n):
    """R-1.5"""
    pass


def squares_sum_odd(n):
    """R-1.6"""
    pass


def squares_sum_odd_2(n):
    """R-1.7"""
    pass


def my_choice(data):
    """R-1.12"""
    pass


def distinct(data):
    """C-1.15"""
    pass


def my_list():
    """C-1.18"""
    pass


def number_of_vowels(s):
    """C-1.24"""
    pass


def only_words(sentence):
    """C-1.25"""
    pass


def correct_arithmetic():
    """C-1.26"""
    pass


# Bônus
def school_pubishment():
    """P-1.34"""
    pass

def question_3():
    input_numbers = input("Insira a sequência de números separadas por espaço:\n")
    list_numbers = input_numbers.split()
    minmax(list_numbers)

def question_4():
    number = int(input("Insira um número inteiro qualquer: "))
    squares_sum(number)

# Chamada da função da questão R-1.3
# question_3()
# Chamada da função da questão R-1.4
question_4()
