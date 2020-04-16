# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('array: ', *array)


mini = 0
maxi = 0
for i, item in enumerate(array):
    if item < array[mini]:
        mini = i
    elif item > array[maxi]:
        maxi = i
print('min: ', array[mini])
print('max: ', array[maxi])
if mini > maxi:
    mini, maxi = maxi, mini
    #print('array_modify: ', *array)

summa = 0
for i in range(mini+1, maxi):
    summa += array[i]
print('sum_item_between: ', summa)