# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum / 4

n = int(input('Введите количество предприятий: '))
# while i < 2:
Company = namedtuple('Company', 'name, total')
Company_aver = namedtuple('Company_aver', 'name, status')
total = 0
info_all = {}
aver_total = 0
company_all = []
company_aver = []
for i in range(n):
    name = input(f'Введите название предприятия: ')
    QUAR = 1
    j = 0
    profit = []
    while j < 4:
        profit.append(int(input(f'Введите прибыль за {QUAR} квартал: ')))
        j += 1
        QUAR += 1
        for k in range(1, 4):
            total = sum(profit)
    info_all.update({name:total})
    aver_total += (total / 4)
    #aver_all = sum(sum_all) / 4
    company_all.append(Company(name, total))

for key, value in info_all.items():
    if value < aver_total:
        stat = f'Прибыль организации меньше среднего {aver_total}'
    else:
        stat = f'Прибыль организации больше среднего {aver_total}'
    company_aver.append(Company_aver(key, stat))

print(company_all)
print(company_aver)