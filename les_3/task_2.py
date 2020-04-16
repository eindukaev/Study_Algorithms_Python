# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'array: {array}')

index_even = []
index_odd = []

for i, item in enumerate(array):
    if item % 2 == 0:
        index_even.append(i)
    else:
        index_odd.append(i)
print(f'index_even: {index_even}', end=' ')
print(f'index_odd: {index_odd}', end=' ')