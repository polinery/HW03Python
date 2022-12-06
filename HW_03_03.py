''' 3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''


def my_func(a, b, c):
    """Принимает три числа, и возвращает сумму наибольших двух из них"""
    numbers = [a, b, c]
    numbers.sort()
    sum_max = numbers[1] + numbers[2]
    return sum_max


print(my_func(int(input('a: ')), int(input('b: ')), c=int(input('c: '))))
