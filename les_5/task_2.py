# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

A = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
dict_a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
n1 = deque(input('Введите первое число: '))
n2 = deque(input('Введите второе число: '))
const = 16


def sum_n(one, two):
    one = one.copy()
    two = two.copy()

    if len(two) > len(one):
        one, two = two, one

    two.extendleft('0' * (len(one) - len(two)))
    i = 0
    resp = deque()
    while len(one) != 0:
        one_e = dict_a[one.pop()]
        two_o = dict_a[two.pop()]
        sum_num = one_e + two_o + i

        if sum_num >= const:
            i = 1
            sum_num -= const
        else:
            i = 0
        resp.appendleft(A[sum_num])

    if i == 1:
        resp.appendleft('1')

    return resp

print(f'{list(n1)} + {list(n2)} = {list(sum_n(n1, n2))}')