# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

RANGE_MIN = 2
RANGE_MAX = 99
R_MIN = 2
R_MAX = 9

for i in range(R_MIN, R_MAX+1):
    COUNT = 0
    for j in range(RANGE_MIN, RANGE_MAX+1):
        if j % i == 0:
            COUNT += 1
    print(f'{i} кратно {COUNT} чисел в интервале от 2 до 99')