profit = int(input('Введите выручку фирмы '))
cost = int(input('Введите издержки фирмы '))
if profit > cost:
    rent = profit / cost
    print('Фирма работает с прибылью. Рентабельность выручки составила ', rent)
    workers = int(input('Введите количество сотрудников фирмы '))
    profwork = profit / workers
    print('Прибыль в расчете на одного сторудника сотавила', profwork)
elif profit == cost:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')