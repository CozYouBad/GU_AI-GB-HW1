a = int(input('Введите результаты пробежки первого дня в км '))
b = int(input('Введите общий желаемый результат в км '))
result_day = 1
result_km = a
while result_km < b:
        result_km = result_km + 0.1 * a
        a = a + 0.1 * a
        result_day = result_day + 1
print('Вы достигнете требуемых показателей на', result_day, 'день')