# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

num = int(input("Введите трехзначное число: "))

first = num // 100
mod = num % 100
second = mod // 10
third = mod % 10
sum = first + second + third
compos = first * second * third

print('Сумма цифр: ', sum)
print('Произведение цифр: ', compos)