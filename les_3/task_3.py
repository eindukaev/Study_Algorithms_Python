# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
print('min: ', mini)
print('max: ', maxi)

array[mini], array[maxi] = array[maxi], array[mini]
print('array_modify: ', *array)